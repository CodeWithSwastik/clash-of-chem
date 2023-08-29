# Clash of Chem: Multiplayer Organic Chemistry Game

Clash of Chem is a thrilling multiplayer game where players compete to convert compounds using reagents in a race to achieve their goals. The game combines strategic thinking, organic chemistry knowledge, and real-time interaction to create an engaging experience.

## Contributing

Contributions are welcome! If you'd like to contribute to Clash of Chem, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request explaining the changes you've made.

### Contributing to reactions.json

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

## License

This project is licensed under the MIT License.
