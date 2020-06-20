<!--Jinja two is the template that flask uses -->
    <!--The Curly Braces and parenthesis acts as a
        code block-->
    
    <!--It works because Flask comes with a parser to interpret the language and make sense of it.
        A parser takes a string that might otherwise has no meaning in HTML or any other language,
        such as {% block pasta %} and converts it into something meaningful. 
        In this case it ultimately outputs HTML.-->

  {% for post in posts %}
    <!--We are looping through the posts and printing we have specified-->

<!--This allows us to override with things that are unique
    to each lage.-->
    {% block content %}{% endblock %}

Note that I had a problem with running my home html file.
I later found out that this was because 
the html comment tag <!-- ... --> does not work in a jinja template.
Take note of this for next time.