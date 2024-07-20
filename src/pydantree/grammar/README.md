To generate the models (`models.py`) for the grammar schema,
install the `datamodel-codegen` dependency group (or pip install
`datamodel-code-generator`) and run the following from `src/pydantree`:

```sh
datamodel-codegen \
  --input data/grammar-schema.json \
  --input-file-type=jsonschema
  --output grammar/models.py \
  --output-model-type=pydantic_v2.BaseModel \
  --enum-field-as-literal=all
```
