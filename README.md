# **Wikipedia_Extractor**

### This Repository will help you get the content and links of all the article related to a particular keyword.

---

## Usage:

This wiki_extractor.py file will take 3 parameter inputs:
 - keyword:- It should be the word for which we want the related pages links to be extracted.
 - num_urls:- Number of related pages ,related to a keyword, that we want.
 - output:- The name of the json file in which the results would be stored.

```cmd
C:\Users\username\Wikipedia_Extractor>python wiki_extractor.py --keyword="Indian Historical Events" --num_urls=10 --output="output.json"
```
Once the above command is executed successfully the output file will be generated ,as follows, in the current directory.

```json
[
    {
        "url":"URL for related page no: 1",
        "content":"Content of the related page no: 1"
    },
    {
        "url":"URL for related page no: 2",
        "content":"Content of the related page no: 2"
    },
    .
    .
    .
    .,
    {
        "url":"URL for related page no: 10",
        "content":"Content of the related page no: 10"
    }
]
```


