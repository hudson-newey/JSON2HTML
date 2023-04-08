# JSON2HTML

Have you ever wanted to write your HTML in JSON format? No?

Well now you can anyways!

## Markup Format

_github-example.json_ (Documented)

```js
{
    // all HTML objects are contained within the "html" tag, notice that none of the contents are contained here, just the tags
    "html": [
        "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'></script>", // LITERAL elements are all elements starting with a '<' tag, this was made so you can import external scripts and stylesheets :)
        "h1 class='display-4'", // basic h1 element with class for unique identification
        "p", // this is an empty element, notice it still has a contents deceleration
        "title", // example website title
        "input type='button' value='Click Me!'" // an empty button without inner text declaration
    ],

    // CSS can be directly written through the "style": [] object
    "style": [
        "h1 { color: red; }",
        "p { color: green }" // css styles are multi lined (for better readability)
    ],

    "script": [
        "console.log('Hello World!');",
        "console.log('If you see this message, JS is enabled!');"
    ],

    "h1 class='display-4'": "This is contents", // the contents of the basic h1 element
    "p": "this is some subtext",
    "title": "Hello World!"
}
```

## Usage

```sh
./JSON2HTML.sh <json_file>
```

## Video Example (Bootstrap Example)

[![asciicast](https://asciinema.org/a/xqWSM82Xgx73xY5ASIC9sxbZq.svg)](https://asciinema.org/a/xqWSM82Xgx73xY5ASIC9sxbZq)
