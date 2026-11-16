# AI Project 3: Tech Stack Recommender

An AI-powered career recommendation system that analyzes users' technical skills and experience to recommend suitable career roles using machine learning and similarity-based ranking techniques.

This project was developed as **Project 3 – AI Recommendation Logic** under the DecodeLabs AI Track.

## Project Overview

The Tech Stack Recommender helps users identify potential career opportunities based on their existing technical skills, experience level, and preferences.

The system processes job postings, extracts relevant technical skills, builds role profiles, and recommends career paths using a content-based recommendation approach.

## Key Features

- **Job Dataset Processing:** Clean, preprocess, and analyze job posting data.
- **Exploratory Data Analysis (EDA):** Analyze job titles, experience requirements, salary distributions, and technology demand.
- **Skill-Based Recommendation:** Recommend career roles based on user-provided technical skills.
- **TF-IDF Vectorization:** Represent skills and job requirements using TF-IDF.
- **Cosine Similarity:** Measure similarity between user skills and career role profiles.
- **Experience Matching:** Adjust recommendations according to the user's experience level.
- **Salary Filtering:** Filter recommended roles based on salary preferences.
- **Skill Gap Analysis:** Identify matching skills and skills users should learn.
- **Cold-Start Recommendations:** Support users with limited skills or incomplete profiles.
- **Interactive Notebook Interface:** Input skills, experience, salary preferences, and recommendation settings.
- **Model Evaluation:** Compare recommendation approaches using Top-K accuracy and Mean Reciprocal Rank (MRR).

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | TF-IDF, similarity calculations, evaluation |
| Matplotlib | Data visualization |
| Regex | Text cleaning and skill extraction |
| IPyWidgets | Interactive notebook interface |
| Google Colab / Jupyter Notebook | Development environment |

## Recommendation Methodology

The recommendation system follows a content-based recommendation approach.

### 1. Data Preprocessing
- Handle missing values.
- Normalize job titles and requirements.
- Extract experience and salary information.
- Remove duplicate and invalid records.

### 2. Feature Engineering
- Extract technical skills from job requirements.
- Tokenize technical terms.
- Generate unigram and bigram features.
- Aggregate job postings into career-role profiles.

### 3. Recommendation Logic
- Convert user skills into TF-IDF vectors.
- Calculate cosine similarity between user profiles and career roles.
- Incorporate experience compatibility.
- Apply salary filtering when requested.
- Rank career roles based on recommendation scores.

### 4. Skill Gap Analysis
For each recommended role, the system identifies:
- Skills already matched by the user.
- Skills the user may need to learn.
- Relevant experience requirements.
- Available salary information.

### 5. Model Evaluation
The notebook evaluates recommendation performance using:
- Top-1 Accuracy
- Top-3 Accuracy
- Top-5 Accuracy
- Mean Reciprocal Rank (MRR)

It also compares TF-IDF cosine similarity with alternative recommendation approaches.

## Recommendation Output

The system provides:

- Recommended career roles.
- Match percentage.
- Similarity score.
- Matched technical skills.
- Skills to learn.
- Experience requirements.
- Salary information.
- Related job posting counts.

> **Note:** Match percentages represent relative recommendation scores, not actual hiring probabilities or guaranteed job eligibility.

## Getting Started

### Option 1: Google Colab

1. Download or clone this repository.
2. Open `Tech_Stack_Recommender.ipynb` in Google Colab.
3. Upload the required dataset.
4. Update the dataset path in the configuration section.
5. Run all notebook cells.
6. Use the interactive recommendation interface.

### Option 2: Jupyter Notebook

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DecodeLabs-Internship.git
cd Project_03
```

Install the required dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib ipywidgets
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook and execute the cells sequentially.

## Project Structure

```text
Tech-Stack-Recommender/
│
├── Tech_Stack_Recommender.ipynb
├── Dataset_jotpars.csv
├── cleaned_jobs.csv
├── README.md
└── .gitignore
```

*Dataset and generated output files may be excluded from the repository depending on their size and distribution permissions.*

## Future Improvements

- Integrate real-time job postings from job platforms.
- Improve technical skill extraction using NLP.
- Add personalized career learning roadmaps.
- Develop a web-based recommendation interface.
- Improve recommendation evaluation using real user feedback.
- Expand the dataset with more job categories and technical skills.

## Author

**Md. Nazibur Rahman**

- GitHub: [nazibur74](https://github.com/nazibur74)

---

⭐ If you find this project interesting, feel free to explore the notebook and its recommendation logic.
