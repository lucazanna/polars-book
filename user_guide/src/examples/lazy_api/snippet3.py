import polars as pl


q3 = pl.DataFrame({"foo": ["a", "b", "c"], "bar": [0.0, 0.1, 0.2]}).lazy()

q3.schema

q3_schema = q3.schema
