from wafp.targets import BaseTarget, Metadata, SchemaSource, SchemaSourceType, Specification, SpecificationType


class Default(BaseTarget):
    def get_base_url(self) -> str:
        return f"http://0.0.0.0:{self.port}/api"

    def get_schema_location(self) -> str:
        return f"http://0.0.0.0:{self.port}/api/swagger.json"

    def is_ready(self, line: bytes) -> bool:
        return b"Starting development server at" in line

    def get_metadata(self) -> Metadata:
        return Metadata.flask(
            flask_version="1.1.2",
            schema_source=SchemaSource(
                type=SchemaSourceType.STATIC,
                library=None,
            ),
            specification=Specification(name=SpecificationType.OPENAPI, version="2.0"),
        )
