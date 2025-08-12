# Web Content Archive

**Original URL:** https://dagster.io/blog/dagster-1-11-build-me-up-buttercup  
**Download Date:** 2025-08-09  
**Content Type:** Blog Post  
**Source Domain:** dagster.io  
**Reason for Download:** Component descriptions and feature analysis for GA strategy research

---

# Dagster 1.11: Build Me Up Buttercup

**Author:** Yuhan Luo  
**Publication Date:** June 26, 2025

## Release Highlights

- **Components (stable)**: Configurable, reusable building blocks in YAML or Python
- **dg CLI (stable)**: New command-line companion for scaffolding and development
- **Cross-platform create-dagster** command
- Quality-of-life improvements in core orchestration and UI
- Ecosystem integrations: Iceberg, dbt Cloud, Airflow, Fivetran
- In-app Integrations Marketplace

## Components (stable): Configurable, Reusable Building Blocks for Data Pipelines

### Key Features

- Plug-and-play in YAML or Python
- Rapid pipeline building with minimal boilerplate
- Ready-made components for:
  - dbt
  - Fivetran
  - Airbyte
  - Sling
  - DLT
  - Power BI

### Highlights

- Automatic documentation generation
- Low-code, high-clarity DSL
- Custom component support
- Powerful tooling with:
  - High-quality errors
  - Strongly typed definitions
  - CI/CD workflow integration

## dg (Stable): All-in-One CLI

### Capabilities

- Code generation
- Local development
- Ad-hoc job execution
- Introspection and validation
- Developer experience utilities

### Features

- `scaffold` for generating definitions
- `dev` to launch Dagster instance
- `launch` for job execution
- `list` and `check` for definition management

## create-dagster: Project Bootstrapper

### Benefits

- Standardized Python directory layout
- Preconfigured local dg CLI setup
- Workspace scaffolding
- No active Python environment required

## UI Enhancements

- Unified asset selection
- Consolidated backfill activity
- Enhanced Asset Graph with health indicators

## Core Orchestration Improvements

- Improved partial retries
- Checks in Ops
- Hooks in Assets
- Efficient backfills and concurrency management

## Integrations

### New and Updated Integrations

- **Fivetran integration (GA)**: Full workspace management capabilities
- **dbt Cloud (Beta)**: Enhanced integration with dbt Cloud platform
- **Apache Iceberg (Preview)**: Support for Iceberg table format
- **Airflow Component (Beta)**: Bridge between Airflow and Dagster workflows
- **Integrations Marketplace (Preview)**: In-app discovery of available integrations

## Community Acknowledgments

The release highlights contributions from over 100 community members, showcasing the collaborative nature of the Dagster project and the growing ecosystem around data orchestration.

## Technical Implementation Notes

### Components Architecture

- Built with configurability as a core principle
- Support for both YAML and Python-based definitions
- Strong typing system for better developer experience
- Automatic validation and error reporting

### CLI Improvements

- Unified command structure for better usability
- Enhanced development workflow support
- Better integration with existing Python tooling
- Cross-platform compatibility improvements

### UI/UX Enhancements

- Streamlined asset selection interface
- Improved visualization of pipeline health and status
- Better management of backfill operations
- Enhanced navigation and discoverability

## Conclusion

Dagster 1.11 "Build Me Up Buttercup" represents a significant leap in data pipeline development, offering more flexibility, ease of use, and powerful integrations. The focus on components, improved CLI tooling, and enhanced UI demonstrates Dagster's commitment to improving the developer experience while maintaining the robust orchestration capabilities that make it a leading data platform.

---

**Note:** This content has been processed and formatted for analysis. All technical details and component descriptions have been preserved to support research and development activities.
