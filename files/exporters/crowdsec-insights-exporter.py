#!/usr/bin/env python3
"""
Digital World CrowdSec Insights Exporter

TODO:
- Read CrowdSec alerts via: cscli alerts list -o json
- Read CrowdSec decisions via: cscli decisions list -o json
- Enrich source IPs with GeoLite2 City
- Enrich source IPs with GeoLite2 ASN
- Export Prometheus metrics:
  - crowdsec_recent_alerts_5m_total
  - crowdsec_recent_alerts_15m_total
  - crowdsec_recent_alerts_60m_total
  - crowdsec_top_source_ip_events
  - crowdsec_top_as_events
  - crowdsec_attack_geo_events
  - crowdsec_attack_as_geo_events
  - digitalworld_server_location
"""

import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer


def build_metrics() -> str:
    lines = []
    lines.append("# HELP crowdsec_insights_exporter_up Exporter health")
    lines.append("# TYPE crowdsec_insights_exporter_up gauge")
    lines.append("crowdsec_insights_exporter_up 1")
    lines.append("")
    lines.append("# TODO: implement CrowdSec, GeoIP and ASN metrics")
    return "\n".join(lines) + "\n"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_response(404)
            self.end_headers()
            return

        body = build_metrics().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9791)
    args = parser.parse_args()

    server = HTTPServer((args.listen, args.port), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
