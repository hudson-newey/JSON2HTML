# JSON2HTML

Have you ever wanted to write your HTML in JSON format? No?

Well now you can anyways!

**Format**
_index.json_ (Documented)
```json
{
    // all HTML objects are contained within the "html" tag, notice that none of the contents are contained here, just the tags
    "html": [
        "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'></script>", // LITTERAL elements are all elements starting with a '<' tag, this was made so you can import external scripts and stylesheets :)
        "h1 class='display-4'", // basic h1 element with class for unique identification
        "p" // this is an empty element, notice it still has a contents decleration
    ],

    // CSS can be directly written through the "style": [] object
    "style": [
        "h1 { color: red; }",
        "p { color: green }" // css styles are multi lined (for better readability)
    ],

    "h1 class='display-4'": "This is contents" // the contents of the basic h1 element
}
```
