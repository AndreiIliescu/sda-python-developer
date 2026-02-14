# ✅ **HTML Beginner Tasks with Explanations (~45 min)**

*You will build a multi-section page with image, video, and form. Terms are explained for beginners.*

---

## **1. Create Your Project Folder & Open it With Live Server**

**Task Requirements**

* Create a folder named `html-practice`.
* Inside it, create a file `index.html`.
* Open the folder with VS Code.
* Right-click `index.html` → **Open with Live Server**.

**Tips**

* **Live Server**: a VS Code extension that refreshes the browser automatically when you save the file.
* Keep your browser open to see live updates.

**New Terms**

* **VS Code**: a code editor for writing HTML, CSS, JS.
* **Folder**: a container for files.

---

## **2. Add the HTML Boilerplate**

**Task Requirements**

* Add: `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>`, `<body>`
* Add a title inside `<title>` describing your page.

**Tips**

* Type `!` + Enter in VS Code to auto-generate.

**New Terms**

* **`<!DOCTYPE html>`**: tells the browser this is an HTML5 document.
* **`<html>`**: root element of the page.
* **`<head>`**: contains metadata (like title, links to CSS).
* **`<body>`**: contains everything visible on the page.
* **`<title>`**: text shown in the browser tab.

---

## **3. Add a Main Page Heading**

**Task Requirements**

* Inside `<body>`, add `<h1>` with the page title (e.g., “My First Webpage”).

**Tips**

* Only **one** `<h1>` per page.

**New Terms**

* **`<h1>`**: top-level heading; represents main title.
* **Heading hierarchy**: `<h1>` → `<h2>` → `<h3>` … smaller headings.

---

## **4. Add a Paragraph**

**Task Requirements**

* Add `<p>` paragraphs describing the page.
* Write 2–3 sentences.

**Tips**

* Use multiple `<p>` tags instead of one long block.

**New Terms**

* **`<p>`**: paragraph; block of text.
* **Block element**: takes up full width, creates a new line.

---

## **5. Create an Unordered List**

**Task Requirements**

* Add `<ul>` with **3–5 `<li>` items**.
* Example: hobbies, favorite foods.

**Tips**

* Keep list items short.

**New Terms**

* **`<ul>`**: unordered list (bullet points).
* **`<li>`**: list item inside a list.

---

## **6. Create an Ordered List**

**Task Requirements**

* Add `<ol>` with 3–5 `<li>` steps (e.g., morning routine).

**Tips**

* `<ol>` automatically numbers items.

**New Terms**

* **`<ol>`**: ordered list (numbers instead of bullets).

---

## **7. Add a Table**

**Task Requirements**

* Create `<table>` with **2 columns** and **3 rows**.
* Fill with simple data (e.g., “Task / Status”).

**Tips**

* Keep content simple.

**New Terms**

* **`<table>`**: container for rows and cells.
* **`<tr>`**: table row.
* **`<td>`**: table cell (data).
* **`<th>`**: table header (optional, bold and centered).

---

## **8. Use `id` and `class` Attributes**

**Task Requirements**

* Give one element a unique `id`.
* Give 2–3 elements a shared `class`.

**Tips**

* Use meaningful names like `id="hero-title"` or `class="highlight"`.

**New Terms**

* **Attribute**: extra information about an element.
* **`id`**: unique identifier for one element.
* **`class`**: group multiple elements for styling or JS.

---

## **9. Create Semantic Layout Sections**

**Task Requirements**

* Add `<header>`, `<main>`, `<footer>`.
* Move existing content:

  * `<header>` → main heading
  * `<main>` → paragraphs, lists, table
  * `<footer>` → simple text

**Tips**

* Semantic tags describe the purpose of content.

**New Terms**

* **Semantic tags**: tell browsers and screen readers what the content means.
* **`<header>`**: top of the page.
* **`<main>`**: main content area.
* **`<footer>`**: bottom section, usually static info.

---

## **10. Build a “Hero” Section**

**Task Requirements**

* Inside `<main>`, create `<section id="hero">` with:

  * `<h2>` heading
  * `<p>` short description

**Tips**

* Hero section is the first content users see.
* Use clear headings.

**New Terms**

* **`<section>`**: logical grouping of content within a page.

---

## **11. Add an Image in the About Section**

**Task Requirements**

* Create `<section id="about">` with heading, paragraph, and an `<img>` element.
* Use an online image URL or local file.
* Add `alt` text.

**Tips**

* `alt` text is important for accessibility.
* Check the `src` path if the image doesn’t show.

**New Terms**

* **`<img>`**: displays an image.
* **`src`**: source URL of the image.
* **`alt`**: alternative text describing the image.

---

## **12. Add a YouTube Video**

**Task Requirements**

* Create `<section id="media">` with heading and `<iframe>` for a YouTube video.
* Use YouTube → Share → Embed.

**Tips**

* Adjust width/height if needed.
* Test playback in Live Server.

**New Terms**

* **`<iframe>`**: embeds another webpage or video.
* **Embed**: insert content from one site into another.

---

## **13. Create a Contact Form**

**Task Requirements**

* Create `<section id="contact">` with a `<form>` containing:

  * Name (`<input type="text">`)
  * Email (`<input type="email">`)
  * Message (`<textarea>`)
  * Submit button (`<button type="submit">Send</button>`)

**Tips**

* Labels make form fields readable.
* No functionality needed yet.

**New Terms**

* **`<form>`**: container for user input.
* **`<input>`**: field for text, email, numbers, etc.
* **`<textarea>`**: multi-line input.
* **`<button>`**: clickable button.

---

## **14. Add a Footer**

**Task Requirements**

* Inside `<footer>`, add copyright text:

  * e.g., “© 2025 My Project”

**Tips**

* Keep footer simple and consistent.

**New Terms**

* Already explained above; `<footer>` is semantic.

---

## **15. Final Review and Clean Up**

**Task Requirements**

* Check all sections display correctly: hero, about (with image), media (video), contact (form), footer.
* Fix any missing closing tags.
* Ensure indentation is clean.

**Tips**

* Good structure makes future styling easier.
* Test everything in Live Server.