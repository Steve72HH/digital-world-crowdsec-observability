# Digital World CrowdSec Observability Stack

A production-ready Prometheus/Grafana/CrowdSec observability stack for monitoring CrowdSec masters, agents, attacks, ASN/provider data, GeoIP attack origins and server health.

## Features

- CrowdSec master and agent monitoring
- Prometheus scraping
- Grafana dashboards
- Node Exporter integration
- CrowdSec Insights Exporter
- GeoIP-ready architecture
- ASN/provider enrichment
- Server location maps
- Ansible deployment

## Planned Dashboard Panels

- Monitored servers
- Servers UP/DOWN
- Recent CrowdSec alerts
- Realtime attack curve
- Top attacker IPs
- Top AS/providers
- Top CrowdSec scenarios
- Global attack origin map
- ASN/provider origin map
- Digital World server location map
- CPU, memory and filesystem usage

## Quick Start

```bash
cp inventory.example.ini inventory.ini
ansible-playbook -i inventory.ini playbooks/deploy_full_stack.yml
