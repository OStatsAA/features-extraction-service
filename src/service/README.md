# Generating protobufs files

```{bash}
python -m grpc_tools.protoc -I src/service/ --python_out=src/service/ --grpc_python_out=src/service --mypy_out=src/service/ src/service/features_extractor_service.proto
```