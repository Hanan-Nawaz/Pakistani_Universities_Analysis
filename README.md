# Pakistani Universities Analysis

![Logo](https://github.com/Hanan-Nawaz/Pakistani_Universities_Analysis/blob/main/Supporting%20Material/logo.png)

## Project Overview

This project involves analyzing the data of Pakistani universities, focusing on various aspects such as the sector (public/private), establishment year, and distribution across provinces. The workflow of this project includes the following steps:

1. **Data Extraction**: 
   - Downloaded the Pakistani Universities dataset from Kaggle.
   - Imported the dataset into a Python environment.

2. **Data Transformation**:
   - Cleaned the dataset by dropping null values.
   - Performed date formatting.
   - Removed unnecessary columns.

3. **Data Loading**:
   - Loaded the cleaned data into a MySQL database, which serves as Data Warehouse.
   - Created a single table in the DW to store the data.

4. **Dashboarding in Tableau**:
   - Created visualizations to explore and present the data:
     - **Sector of Universities**: Displayed a bar chart of public and private universities.
     - **Universities Established Each Year**: Showcased a bar chart illustrating the number of universities established each year.
     - **Universities Table**: Provided a comprehensive table of all universities.
     - **Universities in Each Province**: Visualized the distribution of universities across different provinces in Pakistan.

   - **[View Tableau Dashboard](https://public.tableau.com/app/profile/abdul.hanan.nawaz/viz/Pakistani_Universities_Analysis/Dashboard1)**

## Project Workflow

![Workflow](https://github.com/Hanan-Nawaz/Pakistani_Universities_Analysis/blob/main/Supporting%20Material/workflow.png)

## Screenshots

1. **ETL Process**:
   - Screenshot of VS Code terminal with "ETL Performed Successfully" message.
   - ![ETL Success](https://github.com/Hanan-Nawaz/Pakistani_Universities_Analysis/blob/main/Supporting%20Material/terminal_image.png)

2. **Data Loading Confirmation**:
   - Screenshot of MySQL terminal showing `SELECT * FROM Uni_list LIMIT 10` query result, confirming data load.
   - ![MySQL Data Loaded](https://github.com/Hanan-Nawaz/Pakistani_Universities_Analysis/blob/main/Supporting%20Material/db.png)

## Getting Started

To reproduce this project, follow these steps:

1. Clone the repository.
2. Install the required Python libraries.
3. Execute the ETL script.
4. Import the Tableau dashboard to explore the visualizations.

## Technologies Used

- **Python** for data extraction and transformation.
- **MySQL** (as the Data Warehouse) for data storage.
- **Tableau** for data visualization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
