#!/usr/bin/env python3
"""
OpenAPI 3.1 & AsyncAPI 3.0 Spec Generator from architectural design.json artifacts.
Injects mandatory banking security headers (DPoP, FAPI 2.0, mTLS, CBUAE Correlation IDs).
"""

import argparse
import json
import sys
from pathlib import Path
import yaml

def generate_openapi_spec(design_data: dict) -> dict:
    title = design_data.get("title", design_data.get("artifact_id", "Banking API Service"))
    version = design_data.get("version", "1.0.0")
    description = design_data.get("description", "OpenAPI 3.1 spec generated from architecture design artifact.")
    region = design_data.get("region", "UAE").upper()

    spec = {
        "openapi": "3.1.0",
        "info": {
            "title": title,
            "version": version,
            "description": f"{description} - Region: {region}. Enforces FAPI 2.0 & mTLS security baseline."
        },
        "servers": [
            {"url": "https://api.bank.ae/v1", "description": "Production Regulated Gateway"}
        ],
        "paths": {},
        "components": {
            "securitySchemes": {
                "OAuth2_FAPI2": {
                    "type": "oauth2",
                    "description": "FAPI 2.0 Security Profile with DPoP (Demonstrating Proof-of-Possession)",
                    "flows": {
                        "authorizationCode": {
                            "authorizationUrl": "https://auth.bank.ae/oauth2/authorize",
                            "tokenUrl": "https://auth.bank.ae/oauth2/token",
                            "scopes": {
                                "accounts": "Read account balances and transactions",
                                "payments": "Initiate Sharia & Conventional payment transfers"
                            }
                        }
                    }
                },
                "mTLS": {
                    "type": "mutualTLS",
                    "description": "Mutual TLS for high-assurance B2B/Partner API endpoints"
                }
            },
            "headers": {
                "X-Correlation-ID": {
                    "description": "Mandatory CBUAE/SAMA trace correlation UUID for end-to-end audit trails",
                    "required": True,
                    "schema": {"type": "string", "format": "uuid"}
                },
                "X-Audit-Signature": {
                    "description": "HMAC/DPoP payload signature for non-repudiation",
                    "required": True,
                    "schema": {"type": "string"}
                }
            }
        },
        "security": [
            {"OAuth2_FAPI2": ["accounts", "payments"]},
            {"mTLS": []}
        ]
    }

    # Add endpoints from containers / endpoints if specified in design
    endpoints = design_data.get("endpoints", [
        {"path": "/accounts", "method": "get", "summary": "Retrieve accounts", "bian_domain": "CustomerAccount"},
        {"path": "/payments/transfer", "method": "post", "summary": "Initiate payment transfer", "bian_domain": "PaymentExecution"}
    ])

    for ep in endpoints:
        p_path = ep.get("path", "/resource")
        p_method = ep.get("method", "get").lower()
        p_summary = ep.get("summary", "Execute operation")
        p_domain = ep.get("bian_domain", "CoreBanking")

        if p_path not in spec["paths"]:
            spec["paths"][p_path] = {}

        spec["paths"][p_path][p_method] = {
            "summary": p_summary,
            "description": f"BIAN Service Domain: {p_domain}",
            "parameters": [
                {
                    "name": "X-Correlation-ID",
                    "in": "header",
                    "required": True,
                    "schema": {"type": "string", "format": "uuid"}
                }
            ],
            "responses": {
                "200": {"description": "Successful operation"},
                "400": {"description": "Invalid payload or regulatory validation failure"},
                "401": {"description": "Unauthorized / Invalid DPoP proof"}
            }
        }

    return spec

def generate_asyncapi_spec(design_data: dict) -> dict:
    title = design_data.get("title", design_data.get("artifact_id", "Banking Event Stream"))
    version = design_data.get("version", "1.0.0")

    spec = {
        "asyncapi": "3.0.0",
        "info": {
            "title": title,
            "version": version,
            "description": "AsyncAPI 3.0 event-driven messaging topology generated from architecture design artifact."
        },
        "channels": {
            "paymentEvents": {
                "address": "banking.payments.events.v1",
                "messages": {
                    "PaymentInitiated": {
                        "name": "PaymentInitiatedEvent",
                        "title": "Payment Initiated Event",
                        "summary": "Emitted when a customer or API client triggers a transfer.",
                        "payload": {
                            "type": "object",
                            "properties": {
                                "transactionId": {"type": "string", "format": "uuid"},
                                "amount": {"type": "number"},
                                "currency": {"type": "string", "enum": ["AED", "SAR", "EUR", "USD"]},
                                "shariaCompliant": {"type": "boolean"},
                                "correlationId": {"type": "string", "format": "uuid"}
                            },
                            "required": ["transactionId", "amount", "currency", "correlationId"]
                        }
                    }
                }
            }
        }
    }
    return spec

def export_specs(input_path: str, output_dir: str = "."):
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Design artifact not found: {input_path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    openapi_data = generate_openapi_spec(data)
    asyncapi_data = generate_asyncapi_spec(data)

    out_p = Path(output_dir)
    out_p.mkdir(parents=True, exist_ok=True)

    openapi_file = out_p / "openapi.yaml"
    asyncapi_file = out_p / "asyncapi.yaml"

    with open(openapi_file, "w", encoding="utf-8") as f:
        yaml.dump(openapi_data, f, sort_keys=False, default_flow_style=False)

    with open(asyncapi_file, "w", encoding="utf-8") as f:
        yaml.dump(asyncapi_data, f, sort_keys=False, default_flow_style=False)

    return str(openapi_file), str(asyncapi_file)

def main():
    parser = argparse.ArgumentParser(description="Export design.json to OpenAPI 3.1 & AsyncAPI 3.0 YAML specs.")
    parser.add_argument("input", help="Path to design.json or handoff.json")
    parser.add_argument("-o", "--output-dir", default=".", help="Directory to save generated openapi.yaml and asyncapi.yaml")

    args = parser.parse_args()
    try:
        o_file, a_file = export_specs(args.input, args.output_dir)
        print(f"Successfully generated OpenAPI spec: {o_file}")
        print(f"Successfully generated AsyncAPI spec: {a_file}")
    except Exception as e:
        print(f"Export failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
