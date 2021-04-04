from wafp.targets import BaseTarget, Metadata, SchemaSource, SchemaSourceType, Specification, SpecificationType


class Default(BaseTarget):
    def get_base_url(self) -> str:
        return f"http://0.0.0.0:{self.port}/"

    def get_schema_location(self) -> str:
        return f"http://0.0.0.0:{self.port}/apispec_1.json"

    def is_ready(self, line: bytes) -> bool:
        return b"* Running on" in line

    def get_metadata(self) -> Metadata:
        return Metadata.flasgger(
            flask_version="1.1.2",
            flasgger_version="0.9.4",
            openapi_version="2.0",
        )
