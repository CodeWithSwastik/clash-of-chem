# Clash of Chem

Clash of Chem is a multiplayer online organic chemistry game that you can play with your friends!

## Contribution to reactions.json

If you'd like to add a reaction to reactions.json please follow the following format:

```json
{
  "substrate 1": {
    "reagent 1": "product 1",
    "reagent 2": "product 2"
  }
}
```


Some things to keep in mind:

1. Compound names should be generally be IUPAC names
2. When adding a new compound check whether it is present in the reactions.json, if it is use that name.
3. Compound names should be in LOWERCASE
4. There should only be ONE product (the major product) for each reaction
