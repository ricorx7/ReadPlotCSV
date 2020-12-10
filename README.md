# Read Plot CSV
Read in the data.  This will create a SQLite database file with all the data read in.
Then create plots for this data.  Use the parameters to filter the data for the plots.
The plots will be output using Streamlit and save to HTML file in the same folder as the
data files.  The data will then be exported to CSV.  There will be a CSV file each datatype (Beam, Instrument, Earth and Mag/Dir).

![File Check Loading](http://rowetechinc.co/github_img/file-check-loading.png)

![File Check Summary](http://rowetechinc.co/github_img/file-check-report.png)

![File Check Streamlit](http://rowetechinc.co/github_img/file-check-streamlit.png)

# Install requirements

```commandline
pip install -r requirements.txt
pip install -r rti_python\requirements.txt
pip install -r rti_python_plot\requirements.txt
```

# Run Application 
```commandline
python app.py
```

This version will only create the HTML files and CSV files.  You will not see the data in the web browser.


# Run Application With Streamlit
```commandline
# To just see results
python app.py

# To see plots also
streamlit run app.py
```
This version will create the HTML files and CSV files.  YOu can also view and interact with plots in the Streamlit interface.

