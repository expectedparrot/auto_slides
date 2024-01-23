# Introduction to HTML

- HTML stands for HyperText Markup Language.
- It is the standard language used to create and design web pages.
- HTML documents are made up of elements defined by tags, such as `<html>`, `<head>`, `<body>`, `<div>`, `<p>`, etc.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

# Structure of an HTML Document

- **Doctype Declaration**: The document begins with `<!DOCTYPE html>`, which is an instruction to the web browser about what version of HTML the page is written in.

- **HTML Element**: Following the doctype, the `<html>` element wraps all the content of the entire page and can include a `lang` attribute to specify the language.

- **Head and Body**: Inside the `<html>` tag, there are two main sections: 
  - The `<head>` contains meta-information, links to stylesheets, and scripts.
  - The `<body>` includes the content of the page such as text, images, and other media.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>
</head>
<body>
    <h1>Heading</h1>
    <p>Paragraph</p>
    <!-- More content goes here -->
</body>
</html>
```

# Basic HTML Tags and Their Uses

- `<html>`: This tag represents the root of an HTML document. It is the container for all other HTML elements (except for the `<!DOCTYPE>` tag).

- `<head>`: Contains meta-information about the document, such as its title and link to CSS stylesheets.

```
<head>
    <title>Page Title</title>
</head>
```

- `<body>`: Contains the content of an HTML document, such as text, images, links, etc.

```
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
</body>
```

# Creating Content with HTML

- **Use of Tags**: HTML documents are composed of elements, each defined by tags. A tag, generally, comes in pairs: an opening tag and a closing tag. For example, `<p>` is the opening tag for a paragraph, and `</p>` is the closing tag.

- **Adding Text**: The primary purpose of HTML is to display text content. To add text, simply type it between the opening and closing tags of an element. For example:
  ```html
  <p>This is a paragraph.</p>
  ```

- **Incorporating Multimedia**: HTML allows embedding images, audio, and video. For images, the `<img>` tag is used with the `src` attribute specifying the path to the image file. For example:
  ```html
  <img src="path/to/image.jpg" alt="Description">
  ```

# Linking Pages and Resources in HTML

- **Anchor Tag (`<a>`)**: Used to create hyperlinks to other web pages or resources. Syntax: `<a href="URL">Link Text</a>`

- **Attributes**: Commonly used attributes include `href` (URL of the link), `target` (defines where to open the linked document), and `rel` (specifies the relationship between the current and linked documents).

- **Relative vs Absolute URLs**: Use relative URLs to link to internal resources within the same website (e.g., `<a href="/about.html">About Us</a>`) and absolute URLs for external resources (e.g., `<a href="http://www.example.com">Visit Example</a>`).