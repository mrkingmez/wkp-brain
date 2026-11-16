# Your first web page

About 12 minutes to read, plus about 45 to do the practice

## What you will be able to do

- Make a real web page from a plain text file and open it in your browser.
- Read a few lines of HTML and say what each part does.
- Ask Claude for page code, check it before you use it, and fix a page you broke.

## What you will make

A one-page personal site that lives on your own computer, such as "Five things I love", a page of family recipes, or a garden diary. You will style it with colors, then add a list and a link. It stays on your computer. Nothing in this lesson puts it on the internet.

## What a web page is

Every web page you have ever visited is a text file. Your browser reads the file and draws it on screen. The language in the file is called **HTML**. It is not a programming language in the scary sense. It is a way of labeling text: this part is a heading, this part is a paragraph, this part is a list.

The labels are called **tags**. Most come in pairs: one opens, one closes with a slash.

```html
<h1>Five things I love</h1>
<p>This is a paragraph.</p>
```

`h1` means "the biggest heading". `p` means "paragraph". The browser reads `<h1>` as "start a big heading" and `</h1>` as "end it".

Here is a complete small page. Read it before you use it.

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>My first page</title>
</head>
<body>
  <h1>Five things I love</h1>
  <p>This page lives on my computer. Nobody else can see it.</p>
  <ul>
    <li>Item one</li>
    <li>Item two</li>
  </ul>
</body>
</html>
```

What each part does:

| Part | What it does |
|---|---|
| `<!DOCTYPE html>` | Tells the browser this is a modern web page |
| `<head>` | Holds information about the page that does not show on the page |
| `<title>` | The name that appears on the browser tab |
| `<body>` | Everything you actually see |
| `<ul>` and `<li>` | A bulleted list, and each item in it |
| `<meta charset="UTF-8">` | Helps the browser show letters and symbols correctly |

## Colors and fonts

Looks are handled by a second language called **CSS**. For a one-page site you can put it right inside the page, in the head, between `<style>` tags.

```html
<style>
  body { background-color: #fdf6e3; font-family: Georgia, serif; }
  h1 { color: #7a3b1d; }
</style>
```

Each line says "for this part of the page, set this look". The odd code in `#fdf6e3` is a color. You do not need to memorize colors. You can ask Claude for "a warm cream background and a dark brown heading" and it will give you the codes.

## Which computer do you have?

The steps differ a little, so check before you start. If you see a button with the Windows logo (a window made of four squares) on the bar along the bottom of the screen, you have a **Windows** computer. If you see an Apple logo in the top left corner of the screen, you have a **Mac**. If you are not sure, stop here and ask someone who knows. Do not guess. The tasks below show both.

The tool you need is a **plain text editor**. That is a program that saves exactly the letters you type and nothing else. A word processor such as Word is not the right tool, because it adds hidden formatting that breaks a web page.

- **Windows:** Notepad. Press the Windows key, type Notepad, press Enter.
- **Mac:** TextEdit. Press Command and Space together, type TextEdit, press Enter.

Menus change between versions of both systems, so where a step names a menu, look for the closest name.

## Keep this in your pocket

1. A web page is a text file. HTML labels the parts, and CSS sets the look.
2. Use a plain text editor, and save the file with a name that ends in .html.
3. Read any code Claude gives you before you use it, and ask for HTML and CSS only.

## Practice

Three jobs, about 15 minutes each. You need a browser, your computer's plain text editor, and claude.ai in a tab for Tasks 2 and 3. The free version of Claude is all you need. ChatGPT's free version works for these asks too, and trying the same request in both is a good habit.

Everything below can use made-up or harmless content. This page stays on your computer. If you ever put a page on the internet, everything on it becomes public, so keep private details off any page you plan to share later.

### Task 1: Make the starter page and open it

**Why it matters:** getting a file saved with the right name and opened in a browser is the hardest part. After that it is just editing.

**Do this:**

1. Make a folder for your page. Put it somewhere easy, like Documents. Name it `my-page`. In Windows, open File Explorer, go to Documents, right-click an empty space, and look for New and then Folder. On a Mac, open Finder, go to Documents, and look for New Folder in the File menu.
2. Open your plain text editor (see above). On a **Mac**, TextEdit may start in a fancy mode. Look in the Format menu for **Make Plain Text** and choose it. Menus change, so look for the closest name.
3. Copy the complete small page from earlier in this lesson and paste it in. Change "Item one" and "Item two" to two things you actually love, and add three more list items by copying a `<li>` line.
4. Save it. In **Windows Notepad**, open the File menu, choose Save As, go to your `my-page` folder, type `index.html` as the file name, and if you see a "Save as type" box choose **All files**. Otherwise Windows may quietly name the file `index.html.txt`. On a **Mac**, use Save, name it `index.html`, pick your `my-page` folder, and if it asks about the extension, keep `.html`.
5. Open your folder and double-click `index.html`. It should open in your browser. If it opens in the editor instead, right-click the file (on a Mac, hold Control and click) and look for Open with, then pick your browser. You can also drag the file onto an open browser window.

Copy-paste this line to remind yourself of the exact file name when you save.

```text
index.html
```

**Self-check:**

- [ ] My folder is named `my-page` and the file is named `index.html`.
- [ ] I saved it from a plain text editor, not from a word processor.
- [ ] When I opened it, it showed a big heading and a bulleted list, not a pile of tags.
- [ ] I can say what `<li>` does without looking.

**What good looks like:** a plain, white page with your heading and five list items. It looks basic and that is correct. If you see the tags themselves, like `<h1>`, the file was probably saved as plain text with the wrong ending, or opened in the editor. If the name shows as `index.html.txt`, your computer is hiding the real ending. In Windows File Explorer, look in the View menu for an option to show file name extensions. On a Mac, open Finder, look in its Settings (or Preferences) for the Advanced tab, and turn on the option to show all filename extensions. Menus change, so look for the closest name.

---

### Task 2: Ask Claude to build a page about your topic

**Why it matters:** Claude can write a whole page in seconds. Your job is to ask well, read what comes back, and know what you are putting on your computer.

**Do this:** choose a topic for your page, such as a hobby, a recipe collection, or a garden diary. Ask Claude for a page with a clear request. Say what is on it, what the colors should be, and that you want plain HTML and CSS only, with no JavaScript and nothing that loads from the internet.

```text
I am making my first web page and I am a beginner. Please write one complete
HTML file about [your topic]. It should have a big heading, a short intro
paragraph, a bulleted list of five things, and a warm, simple color scheme
with the CSS inside a style tag in the head. Use plain HTML and CSS only: no
JavaScript, and nothing that loads files from the internet. After the code,
explain in plain words what each part does.
```

Before you use anything, read the code. You do not need to understand every line. Look for any line that says `<script` or a web address you did not ask for. If you see either one, ask Claude: "What does this line do, and can you remove it?" Then copy the code, paste it into a new plain text file, save it as `second.html` in your `my-page` folder, and open it in the browser.

**Self-check:**

- [ ] I asked for plain HTML and CSS only.
- [ ] I read the code before I saved it, and looked for `<script` and unfamiliar web addresses.
- [ ] I asked Claude to explain at least one line I did not understand.
- [ ] The page opens in my browser and looks the way I asked.

**What good looks like:** a page that looks noticeably better than your starter. If it is not what you pictured, ask Claude for one change at a time, such as "make the heading bigger" or "use a blue background". One change per request makes it easy to see what each did. After each change, save the file, go to your browser tab, and reload the page (the circular arrow, or press F5 on Windows or Command and R on a Mac).

---

### Task 3: Change it yourself, then break it on purpose

**Why it matters:** the day something looks wrong, you will want to know you can find the cause. Breaking a page you understand is how you learn to repair one.

**Do this:** open `index.html` again. Do these in order, saving and reloading after each.

1. Change the heading text to your own words.
2. Add a link under the list. This line shows a link whose clickable words are "A site I like". Swap in a real site's address and your own words.

```html
<p><a href="https://example.com">A site I like</a></p>
```

3. Add a `<style>` block from earlier in this lesson, between `<head>` and `</head>`, and change one color.
4. Now break it. Delete one closing tag, for example the `</h1>`. Save, reload, and look at what happens.
5. Copy the whole broken page and send it to Claude. Fix it by asking.

```text
This HTML page looks wrong in my browser. Here is the whole file:
[paste it]
What is wrong with it? Tell me the line first, then give me the corrected
file. Use plain HTML only.
```

Compare Claude's fixed version to yours and find the one tag that was missing.

**Self-check:**

- [ ] I changed the heading, added a link, and changed a color.
- [ ] I deleted a closing tag on purpose and saw what it did to the page.
- [ ] Claude pointed to the line with the problem.
- [ ] I fixed my file and the page looks right again.

**What good looks like:** a page with your own words, a working link, a color you picked, and a tag problem you saw break the page and fixed yourself. Claude may find the missing tag quickly. If it names a different problem, check the line it names and ask why. You are now the person who can tell when a page is right.

When you have done the tasks, press the practice button below. It saves that you finished and opens the next lesson. Passing the quiz with 2 of 3 right opens it too.

<div id="practice-done"></div>

## Further reading

These are optional. They go to outside pages that were not read for this lesson. Read what they say today, since sites change.

- MDN Web Docs, a reference site for people who build web pages: [https://developer.mozilla.org](https://developer.mozilla.org)
- Claude, from Anthropic: [https://claude.ai](https://claude.ai)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and the next lesson opens.

<div id="quiz"></div>
