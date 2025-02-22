def test_run(fuzzer):
    result = fuzzer.start("http://127.0.0.1:1/openapi.json", "http://127.0.0.1:1/")
    assert result.completed_process.returncode != 0
    assert b"curl: (7) Failed to connect to 127.0.0.1 port 1: Connection refused" in result.completed_process.stdout
    artifacts = result.collect_artifacts()
    assert len(artifacts) == 1


def test_without_volumes(fuzzer):
    # Docker-compose volumes are optional for `docker-compose run` and can be omitted if needed
    result = fuzzer.compose.run("fuzzer", ["http://127.0.0.1:1/openapi.json"])
    # And the resulting args to `docker-compose` do not contain volumes
    assert result.args == [
        "docker-compose",
        "-f",
        "docker-compose.yml",
        "-p",
        "wafp_example_fuzzer",
        "run",
        "fuzzer",
        "http://127.0.0.1:1/openapi.json",
    ]
