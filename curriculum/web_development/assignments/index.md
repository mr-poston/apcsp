# Web Development

* Recall that we discussed HTTP in the context of internet technologies and HTML in the context of web development. What’s the difference between HTTP and HTML?

* Recall that we discussed both HTML and CSS in the context of web development. What’s the difference between HTML and CSS?

* For this challenge, you might find it helpful to skim or search http://htmldog.com/guides/html/ and http://htmldog.com/guides/css/, which build upon concepts from lecture.

    Visit [this sandbox](sandbox.cs50.io/?window=browser&window=terminal&window=editor&file=index.html&file=styles.css), logging in via GitHub if prompted, to create a CS50 Sandbox (a small web-based development environment) containing files called `index.html` and `styles.css`, both initially empty, pre-created for you.

    Now let’s have you make an actual website with multiple pages. To test that your website is behaving as expected, in the terminal window at the bottom you can type `http-server`, which will then allow you to use the embedded browser viewer on the right to view your page.

    We’ll leave its design largely up to you, subject only to the following requirements:

    1. Your website’s main page should live in `index.html`, since most web servers serve up `index.html` by default, in the absence of an explicit file name in a URL.
    2. Your website must include a least one other page with a similar amount of content (with any filename, so long as it ends in .html), and your website’s main page (i.e., `index.html`) must somehow link to that page. You can click the little folder icon at the window’s top-left to open the file tree, then the “+” to add additional files or folders in your Sandbox.
    3. Your website should use relative, and not absolute, links.
    4. Your website must include at least one image. Note that the above instructions for creating new files also allow you to upload files, though you may also use images already on the internet.
    5. Your website must be stylized with at least some CSS, which must live in styles.css (an “external stylesheet”), just as we saw (briefly) in css4.html. Your stylesheet should utilize at least a handful of CSS properties.
    6. Your website should be more complex than those from class (but much less complex than Harvard’s home page!). As such, your website should probably use several dozen HTML tags overall.

    Alright, make us proud!

    When done, click “Share”. Take care not to close your sandbox before making note of its URL, lest you lose work!

    To view (and thus test!) your web page, remember to run `http-server` in your sandbox’s terminal window, and then reload the embedded browser via the icon to the left of “localhost:8080”.