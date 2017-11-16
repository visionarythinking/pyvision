try:
    from google import search
    import webbrowser
    
except ImportError: 
    print("No module named 'google' found")
 
# to search
query = "steuererklärung tipps pauschalbeträge filetype:pdf"
 
for j in search(query, tld="de",lang="de", num=10,start=1, stop=100, pause=3):
    print(j)
    webbrowser.open_new_tab(j) 
