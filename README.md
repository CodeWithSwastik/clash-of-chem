# Clash of Chem
It's Clash of Code, but Organic Chemistry.

## Concept UI
![image](https://user-images.githubusercontent.com/61446939/189540221-0d1309c9-caf4-4c10-823e-56eafaf33fe2.png)

## Contribution to reactions.json
If you'd like to add a reaction to reactions.json please follow the following format:
```json
{
  "substrate 1": 
      {
         "reagent 1": "product 1",
         "reagent 2": "product 2",
      }
}
```

Some things to keep in mind:
1. Compound names should be preferred IUPAC names and not common names
2. Compound names should be in LOWERCASE
3. There should only be ONE product (the major product) for each reaction
