
# What is a Web Browser?

Web Browser is a software Application used to process information that retrieve from World Wide Web. 

e.g. when you search for a keyword in search engine (Application used to index the searched keyword) like Google,Bing etc. It sends back data which is in the from of MarkUp language. Web Browser renders this information and make it a useful content for the user like us.

From the above information, it can be concluded that Web Browser is used to render information which is in the form of text, images, video, gifs etc. And this information is then presented to us using Web Browser which gives the meaning to it.




## Components of Web Browser
The browser main component are 

 - The user Interface

    This includes the address bar, back/forward button, bookmarking menu, etc. Every part of the browser display except the window where you see the requested page.

 - The browser engine

    Marshals actions between the UI and the rendering engine.
 - Rendering engine

    Responsible for displaying requested content. For example if the requested content is HTML, the rendering engine parses HTML and CSS, and displays the parsed content on the screen.

 - Networking

    For network calls such as HTTP requests, using different implementations for different platform behind a platform-independent interface.

 - UI backend

    Used for drawing basic widgets like combo boxes and windows. This backend exposes a generic interface that is not platform specific. Underneath it uses operating system user interface methods.

 - JavaScript interpreter

    Used to parse and execute JavaScript code.

 - Data Storage

    This is a persistence layer. The browser may need to save all sorts of data locally, such as cookies. Browsers also support storage mechanisms such as localStorage, IndexedDB, WebSQL and FileSystem.
    
![App Screenshot](https://s3-whjr-curriculum-uploads.whjr.online/2b83f3b8-0062-4476-8239-e32eac66bd8b.PNG)

## Understanding the Role of Rendering Engine in Browsers


Once a user requests a particular document, the rendering engine starts fetching the content of the requested document. This is done via the networking layer. The rendering engine starts receiving the content of that specific document in chunks of 8 KBs from the networking layer. After this, the basic flow of the rendering engine begins.

![render image](https://s3-whjr-curriculum-uploads.whjr.online/e00f12fb-743c-4db4-bee5-1fadba7a1da6.PNG)

## The four basic steps include:
- The requested HTML page is parsed in chunks, including the external CSS files and in style elements, by the rendering engine. The HTML elements are then converted into DOM nodes to form a “content tree” or “DOM tree.”

- Simultaneously, the browser also creates a render tree. This tree includes both the styling information as well as the visual instructions that define the order in which the elements will be displayed. The render tree ensures that the content is displayed in the desired order.

- Further, the render tree goes through the layout process. When a render tree is created, the position or size values are not assigned. The entire process of calculating values for evaluating the desired position is called a layout process. In this process, every node is assigned the exact coordinates. This ensures that every node appears at an accurate position on the screen.

- The final step is to paint the screen, wherein the render tree is traversed, and the renderer’s paint() method is invoked, which paints each node on the screen using the UI backend layer.


## Parser

Before starting with the concept, let’s go through the terminology in detail. The word parsing means to divide something into its components and then describe their syntactic roles. The word processing is a familiar word and stands for dealing with something using a standard procedure. Combined these two explain how HTML parser works in generating DOM trees from text/html resources.


Parser is a compiler that is used to break the data into smaller elements coming from lexical analysis phase.
A parser takes input in the form of sequence of tokens and produces output in the form of parse tree.

Parsing is of two types: top down parsing and bottom up parsing.
![](https://s3-whjr-curriculum-uploads.whjr.online/e7b2e32a-d0fe-405b-8ae5-8dc35aca8ad9.PNG)

## Top down Parsing

- The top down parsing is known as recursive parsing or predictive parsing.

- Bottom up parsing is used to construct a parse tree for an input string.

- In the top down parsing, the parsing starts from the start symbol and transform it into the input symbol.

Parse Tree representation of input string "acdb" is as follows:

![](https://s3-whjr-curriculum-uploads.whjr.online/24e59bfa-04fc-42ee-8f45-11bf513d0f3c.PNG)


## Bottom Up parsing

- Bottom up parsing is also known as shift-reduce parsing.
- Bottom up parsing is used to construct a parse tree for an input string.
- In the bottom up parsing, the parsing starts with the input symbol and construct the parse tree up to the start symbol by tracing out the rightmost derivations of string in reverse.


## Script Processor

The script processor executes Javascript code to process an event. The processor uses a pure Go implementation of ECMAScript 5.1 and has no external dependencies. This can be useful in situations where one of the other processors doesn’t provide the functionality you need to filter events.

The processor can be configured by embedding Javascript in your configuration file or by pointing the processor at external file(s).

![script processor](https://s3-whjr-curriculum-uploads.whjr.online/32e47eef-ed03-4325-b944-afd11fd88ca2.PNG)


## Tree construction 

Tree construction is based on parent-child relation.

consider this example.

```bash
    <html>
      <head>
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <title>Critial Path: Hello world!</title>
      </head>
      <body>
        <div style="width: 50%">
          <div style="width: 50%">Hello world!</div>
        </div>
      </body>
    </html>
```
![tree](https://s3-whjr-curriculum-uploads.whjr.online/d6a4311a-52ee-4228-b1c2-129944acac6e.PNG)


## Order of script execution

Executable objects go through four execution stages. The second one is the generation stage. Scripts are generated during this stage. The time at which the script is generated depends on object attributes. The order in which scripts are processed in an object depends on which Process pages the scripts are on.

This page includes the following:

- Execution stage

    Executable objects go through four execution stages. The second one is the generation stage. Scripts are generated during this stage. The time at which the script is generated depends on object attributes. The order in which scripts are processed in an object depends on which Process pages the scripts are on.

- Time of processing

    The time at which the script is generated depends on the Generate Task at attribute that you define on the object Attributes page.

- Order of processing

    Depending on the type of object, the task may have more than one Process page on which you can write scripts.
    - Pre process
    - Child post process
    - Post process

- Processing in script

    The Browser Engine processes scripts line by line. 



## Layout and Printing

This can be understood with the help of a book layout. A book has the information which are arranged in a order.
Layout in browser means the same. How different element will render and where will be the location.

The following is the layout of printing page. Here with this example we will try to understand,
how layout has done it's job. 

On the left all the functionality is given such as:
- New,Save, share, publish, etc.

On Mid, attributes are listed such as:
- which printer to connect.
- number of copies to be printed.
- orientation of printing page.

All these are defined.

And lastly, On the right, the final layout is rendered which shows the final page image which is goint to be printed.

![print layout](https://s3-whjr-curriculum-uploads.whjr.online/aaf46880-4796-454d-9c1b-e505b61a7203.PNG)