# ![-+@](img/rose24.png) Rose

Rose is a tree representation that simply uses rows of indented text. Nested objects, dictionaries, lists, and whatever weird nonsense TOML is doing are too much clutter; knock it off, y'all.

This is an experimental attempt to translate back and forth between a tree format that's easy to read and write and a tree format that Python understands. It is intended to be for trees what markdown is for web pages: less distracting boilerplate but without the imprecision and guesswork of WYSIWYG.

## Syntax

Rose has 3 main rules:

- Each line is the child of the nearest line with a lower indentation level above it.

- Direct children may optionally be placed on the same line as their parent instead, separated by tabs.

- An optional `-+@` or `--@` header can take flags to change the rules if the defaults don't fit the application or your sensibilities. Flags can be added in the future to extend the language without breaking old trees.

For now, all data values are strings. If you need anything else, you'll have to convert it yourself. Automatic translation to native data types is on the to-do list.

## Examples

### Recipe

```
Just the Marshmallows
  ingredients:
    cereal marshmallows
    either
      moo milk
      rice milk
  instructions:

    Dump the marshmallows into a bowl. Don't put in so much you'll get sick, but do eat a serving large enough to properly honor the memory of your childhood self.

    Add milk. You can probably get away with less than you'd use in regular cereal.

    Take a photo of your dinner before eating it, so you can send it to your parents to show off your heroism. True adulthood is living your own life, not the one your parents prescribed for you.
```

### To-do list

```
achieve contentment
	eat marshmallows for dinner
		buy milk
		✓	buy marshmallows
	take over the world
		become immortal
			study biology
			learn linear algebra
		study supply chain management
		x	practice evil laugh
```

## Background

Visualizing data as an indented tree makes it easy to comprehend:

```
grandparent
|
+-> parent
    |
    +-> child
    |   |
    |   +-> grandchild
    |
    +-> sibling
```

Compare the legibility of the same structure in JSON:

```json
{
  "children": [
    {
      "children": [
        {
          "children": [
            {
              "children": [],
              "content": "grandchild"
            }
          ],
          "content": "child"
        },
        {
          "children": [],
          "content": "sibling"
        }
      ],
      "content": "parent"
    }
  ],
  "content": "grandparent"
}
```

Even hiccup syntax is only nice to work with to the extent that it imitates a straightforward tree diagram:

```edn
[:grandparent
 [:parent
  [:child
   [:grandchild]]
  [:sibling]]]
```

If you are stuck waiting for structure editors to take off and have to deal with tree structures in monospaced text grids in the mean time, how would you ideally like to do it?

Well, maybe we can just type the tree using indentation but without the pipes:

```
grandparent
  parent
    child
      grandchild
    sibling
```

This also has the advantage that indentation-based folding is already supported in sufficiently fancy text editors.

# See also

- DOT (Graphviz)
- edn
- JSON
- JSONL / JSON lines
- Markdown
- Pollen (Racket)
- S-Expressions
- S-XML
- TOML
- XML
- YAML
