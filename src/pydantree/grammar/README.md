To generate the models (`models.py`) for the grammar schema,
install the `datamodel-codegen` dependency group (or pip install
`datamodel-code-generator`) and run the following from `src/pydantree`:

```sh
datamodel-codegen --input data/grammar-schema.json --output grammar/models.py
```
