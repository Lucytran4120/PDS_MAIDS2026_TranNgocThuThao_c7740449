# PDS_MAIDS2026_TranNgocThuThao_c7740449

Coursework repository for **PDS** (MAIDS 2026 cohort).

- **Student:** Tran Ngoc Thu Thao
- **Student ID:** c7740449

This repo holds my weekly practice code and notes for learning **NumPy** and **pandas**. The comments in the code are written in Vietnamese (without diacritics in places) and are my own study notes.

## Repository contents

| File | Description |
| --- | --- |
| `week 2.py` | Week 2 practice script: NumPy and pandas basics (see below). Most examples are commented out so they can be run one at a time. |
| `du_lieu.npy` | NumPy binary file (`[1 2 3]`, int64) produced by `np.save` in the Week 2 exercises. |
| `bang.csv` | Plain-text CSV (values 1, 2, 3) produced by `np.savetxt` in the Week 2 exercises. |
| `.idea/` | PyCharm project settings (not needed to run the code). |

## Week 2 topics (`week 2.py`)

**NumPy**
- Creating arrays: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace` (and the difference between `arange` and `linspace`)
- Indexing and slicing for 1D and 2D arrays, including negative steps
- Boolean masking: filtering and replacing values by condition, and using `.copy()` to keep the original data
- `reshape`, including `-1` for an inferred dimension
- The `axis` argument (sums by column vs by row)
- Summary statistics: `sum`, `mean`, `median`, `max`, `min`, `argmax`, `argmin`, `std`
- Random numbers with `np.random.default_rng(seed)`: `random`, `integers`, `normal`, `choice`
- Broadcasting
- Saving and loading data: `np.save` / `np.load`, `np.savetxt` / `np.loadtxt`

**pandas**
- Building a `DataFrame` with custom row labels (`index`) and column names
- Selecting rows and columns with `.loc` and `[]`
- Adding a computed column (average score per student)
- Reference notes: `read_csv`, filtering, `sort_values`, `groupby`, `to_excel`, `head`, `tail`, `shape`, `dtypes`, `info`, `describe`

## Requirements

- Python 3.9+
- [NumPy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)

```bash
pip install numpy pandas
```

## Running the code

```bash
git clone https://github.com/Lucytran4120/PDS_MAIDS2026_TranNgocThuThao_c7740449.git
cd PDS_MAIDS2026_TranNgocThuThao_c7740449
python "week 2.py"
```

The file name contains a space, so keep the quotes around it.

Most NumPy examples are commented out. To try one, remove the leading `#` from the lines you want. Several examples reuse the array `a`, so uncomment its definition first (for example `a = np.array([4, 8, 6, 2, 10])`).

Once `a` is defined, the script prints a small `DataFrame` of scores for two students (An and Bình) in Toán, Văn and Anh, followed by Bình's row, the Toán column, and the average column (`TB`).

## Notes

- The script currently contains an uncommented `np.sum(a)` line while the definition of `a` is commented out. Uncomment `a` (see above) before running, or the script will stop with a `NameError`.
