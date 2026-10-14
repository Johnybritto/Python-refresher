"""R23-C13 — Kubernetes Pod JSON health report.

Problem statement
-----------------
Given an iterable of JSON lines, produce a health report for Kubernetes Pods.
Each valid line must decode to an object with:

- ``metadata.name``: a non-empty string;
- ``status.phase``: a string; and
- ``status.containerStatuses``: a list of objects, each having a boolean
  ``ready`` field.

A valid Pod is healthy only when its phase is ``"Running"``, it has at least
one container status, and every container is ready.  Any valid Pod that does
not meet those conditions is unhealthy.

Ignore no input: malformed JSON and invalid Pod records are counted in
``invalid_pods``.  Return a report with the total number of valid Pods, the
number of healthy Pods, and unhealthy Pod names in input order.

Sample input
------------
    {"metadata":{"name":"api-1"},"status":{"phase":"Running","containerStatuses":[{"ready":true}]}}
    {"metadata":{"name":"worker-1"},"status":{"phase":"Pending","containerStatuses":[]}}

Sample output
-------------
    {
        "total_pods": 2,
        "healthy_pods": 1,
        "unhealthy_pods": ["worker-1"],
        "invalid_pods": 0,
    }

Target complexity: O(C) time for C input characters and O(U) extra space for
the returned list of U unhealthy Pod names.  Process the input one line at a
time; do not call ``read()`` or ``readlines()``.
"""

import json
from collections.abc import Iterable


def pod_health_report(lines: Iterable[str]) -> dict:

    invalid_pods= 0
    total_pods = 0
    healthy_pods = 0
    unhealthy_pods = []

    for line in lines:
        try:
            pod = json.loads(line)
        except json.JSONDecodeError:
            invalid_pods +=1
            continue

        if not isinstance(pod, dict):
            invalid_pods +=1
            continue

        metadata = pod.get("metadata")
        status  = pod.get("status")

        if not isinstance(metadata, dict) or not isinstance(status, dict):
            invalid_pods +=1
            continue

        name = metadata.get("name")
        phase = status.get("phase")


        containers = status.get("containerStatuses")

        valid_fields= (
            isinstance(name, str)
            and name != ""
            and isinstance(phase, str)
            and isinstance(containers , list)
        )
        if not valid_fields:
            invalid_pods +=1
            continue

        valid_containers = True

        for container in containers:
            if not  isinstance(container, dict) or not isinstance(container.get("ready"), bool):
                valid_containers=False
                break

        if not valid_containers:
            invalid_pods +=1
            continue


        if phase == "Running" and containers and all(container["ready"] is True for container in containers):
            healthy_pods +=1
            total_pods +=1
        else:
            total_pods +=1
            unhealthy_pods.append(pod["metadata"]["name"])

    return {
        "total_pods": total_pods,
        "healthy_pods": healthy_pods,
        "unhealthy_pods": unhealthy_pods,
        "invalid_pods" : invalid_pods
    }


    """Return aggregate Pod health information from JSON-lines input.

    Treat malformed JSON, non-object records, and records missing or violating
    any required field from the problem statement as invalid.
    """
    raise NotImplementedError("Implement R23-C13 before running checks")


def run_tests() -> None:
    healthy_api = (
        '{"metadata":{"name":"api-1"},"status":{"phase":"Running",'
        '"containerStatuses":[{"name":"api","ready":true},'
        '{"name":"sidecar","ready":true}]}}'
    )
    pending_worker = (
        '{"metadata":{"name":"worker-1"},"status":{"phase":"Pending",'
        '"containerStatuses":[]}}'
    )
    unready_cache = (
        '{"metadata":{"name":"cache-1"},"status":{"phase":"Running",'
        '"containerStatuses":[{"name":"cache","ready":false}]}}'
    )

    assert pod_health_report([healthy_api, pending_worker, unready_cache]) == {
        "total_pods": 3,
        "healthy_pods": 1,
        "unhealthy_pods": ["worker-1", "cache-1"],
        "invalid_pods": 0,
    }
    assert pod_health_report(iter(())) == {
        "total_pods": 0,
        "healthy_pods": 0,
        "unhealthy_pods": [],
        "invalid_pods": 0,
    }

    invalid = [
        "not json",
        "[]",
        '{"metadata":{"name":""},"status":{"phase":"Running","containerStatuses":[]}}',
        '{"metadata":{"name":"api"},"status":{"containerStatuses":[]}}',
        '{"metadata":{"name":"api"},"status":{"phase":"Running","containerStatuses":[{"ready":"yes"}]}}',
        '{"metadata":{"name":"api"},"status":{"phase":"Running","containerStatuses":"none"}}',
    ]
    assert pod_health_report(invalid) == {
        "total_pods": 0,
        "healthy_pods": 0,
        "unhealthy_pods": [],
        "invalid_pods": 6,
    }

    no_containers = (
        '{"metadata":{"name":"empty-1"},"status":{"phase":"Running",'
        '"containerStatuses":[]}}'
    )
    assert pod_health_report([no_containers]) == {
        "total_pods": 1,
        "healthy_pods": 0,
        "unhealthy_pods": ["empty-1"],
        "invalid_pods": 0,
    }

    generator = (line for line in [healthy_api, "bad json", pending_worker])
    assert pod_health_report(generator) == {
        "total_pods": 2,
        "healthy_pods": 1,
        "unhealthy_pods": ["worker-1"],
        "invalid_pods": 1,
    }
    print("All R23-C13 checks passed")


if __name__ == "__main__":
    run_tests()
