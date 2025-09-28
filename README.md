# BibTeX Field Cleaner

A lightweight Python script to **clean unwanted fields** (like `url`, `issn`, `doi`) from your `.bib` files.  
Perfect for keeping your references neat before journal submission or when you want to simplify BibTeX entries.

---

## Features

- Remove any specified BibTeX fields (not just `url`)
- Handles multiple fields at once (`url`, `issn`, `doi`, etc.)
- Cleans up extra blank lines and dangling commas
- Simple, fast, no dependencies outside the Python standard library

---

## Usage

1. Clone this repo:

   ```bash
   git clone https://github.com/breezy-codes/bibtex-field-cleaner.git
   cd bibtex-field-cleaner
    ```

2. Edit the script (`bibcleaner.py`) to set:

   ```python
   input_file = "references.bib"
   output_file = "references_cleaned.bib"
   fields_to_remove = ["url", "issn"]
   ```

3. Run it:

   ```bash
   python bibcleaner.py
   ```

Your cleaned `.bib` file will be saved as `references_cleaned.bib`.

---

## Example

**Input:**

```bibtex
@article{Ngo2024_RAN,
  title = {RAN Intelligent Controller},
  author = {Ngo, Mao V. and Quek, Tony Q.S.},
  year = {2024},
  journal = {ICT Express},
  url = {https://doi.org/10.xxxx/icte.2024.02.001},
  issn = {2405-9595},
}
```

**After cleaning (`url`, `issn` removed):**

```bibtex
@article{Ngo2024_RAN,
  title = {RAN Intelligent Controller},
  author = {Ngo, Mao V. and Quek, Tony Q.S.},
  year = {2024},
  journal = {ICT Express},
}
```

---

## Extending

Want to remove other fields? Just add them to the list:

```python
fields_to_remove = ["url", "issn", "doi", "publisher"]
```

---

## License

This project is released under the **GNU General Public License v3.0**.
Feel free to use, modify, and share.

---

Clean up your `.bib` files and keep your references submission-ready!
