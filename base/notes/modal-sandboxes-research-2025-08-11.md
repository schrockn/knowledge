# Modal Sandboxes Research
*Date: 2025-08-11*

## Overview
Research into Modal sandbox capabilities, runtime limits, and practical considerations for building a platform service.

## Key Findings

Modal sandboxes provide a flexible execution environment with configurable timeout limits. Unlike having a fixed maximum lifetime, sandboxes are controlled through per-command execution timeouts specified via the `timeout` parameter when using `sb.exec()`. Each individual command inside the sandbox will be terminated if it runs longer than the specified timeout, which can range from 1 second to approximately 24 hours per command execution.

The default timeout for Modal functions is 5 minutes, but this can be overridden based on needs. Sandboxes themselves don't have a hard lifetime limit - they're controlled by the command timeouts and manual termination decisions.

## Practical Implementation Patterns

A common and effective pattern is maintaining a pool of sandboxes available for executing tasks as they arrive. You can keep a list of object_ids of sandboxes that are "open" and reuse them across multiple requests. This approach would be particularly valuable for a platform service, allowing you to keep warm sandboxes ready for common runtime configurations, reuse sandboxes across multiple user requests with proper isolation, and terminate and recreate sandboxes periodically for security purposes.

For long-running services, you can run them in sandboxes by passing entrypoint arguments directly to the Sandbox constructor. This is useful for keeping services running in the background, with timeouts configurable up to 24 hours.

## Handling Extended Workloads

For workloads that might exceed the 24-hour individual function limit, Modal recommends making jobs interruptible and resumable through checkpointing. While this pattern is commonly shown with training jobs, the same approach could apply to any user code that needs to run for extended periods. The key is implementing restart mechanisms that automatically respawn sandboxes before hitting the 24-hour limit.

## Service Design Considerations

From a service architecture perspective, the configurable timeout approach enables offering different tiers based on execution duration needs. Quick executions for development and testing could use shorter timeouts, standard workloads could run for hours, and premium long-running services could utilize the full 24-hour capacity. Pricing models could naturally tie longer runtimes to higher tiers to manage infrastructure costs effectively.

The flexibility of per-command timeouts means you can adjust limits based on user needs and your platform's pricing model, while the sandbox pooling strategy helps optimize resource utilization and reduce cold start latencies.

## Application to GRPC Service Scenario

For a service where users push code that runs as GRPC services with agent-based reconciliation, Modal sandboxes present an intriguing alternative to traditional container orchestration. The key architectural question is whether Modal's sandbox model aligns with the reconciliation pattern you're using.

Modal sandboxes could potentially replace your K8s/ECS infrastructure by running each user's GRPC service inside a sandbox with appropriate port forwarding and network configuration. The agent could maintain sandbox pools instead of container instances, using Modal's API to create, monitor, and terminate sandboxes as needed. Since your services can be terminated and restarted when needed (with cached state being acceptable to lose), this maps well to Modal's execution model.

However, there are some considerations. Your reconciliation agent would need to integrate with Modal's API rather than Kubernetes or ECS APIs, which represents a significant architectural shift. The 24-hour maximum runtime could be a constraint if any user services need to run continuously for longer periods, though your restart-friendly design mitigates this concern.

The introspection requirements for checking service state would need to work through Modal's sandbox networking model. You'd need to verify that GRPC services can be properly exposed and that your tooling can connect to services running inside sandboxes for both health checks and actual service invocation.

Modal sandboxes might be particularly attractive if you're dealing with highly variable workloads or want to reduce infrastructure management overhead. The automatic scaling and serverless nature could simplify your agent's reconciliation logic, potentially reducing it from managing container lifecycles to simply ensuring the right sandboxes exist for active user services.