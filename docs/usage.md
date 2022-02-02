# Example Usage

Maybe not yet ... but if you insist:

## Call without arguments

```console
$ gengive
Usage: gengive [OPTIONS] COMMAND [ARGS]...

  Render text (Danish: gengive tekst).

Options:
  -V, --version  Display the gengive version and exit  [default: False]
  -h, --help     Show this message and exit.

Commands:
  render   render the manuscript for target.
  version  Display the gengive version and exit
```

## Version command

```console
$ gengive version
Render text (Danish: gengive tekst). version 2022.2.2
```

## Render command

### Dry run

```console
$ gengive render examples/bar/ --dry-run
Note: Dry run - verification mode.
Updating publisher root from /somewhere/gengive to examples ...
Retrieving manuscript folders below publisher root examples ...
- bar
Identifying variants defined for document(bar) ...
- default
Requested rendering document(bar) for target(default) below /somewhere/gengive/render/bar/default/ ...
Binder analysis OK, all files resolve. Sequence of binding will be:
 1: examples/bar/foo.md
{
  "request_parameters": [
    "verify",
    "examples/bar/",
    "default"
  ],
  "processing_start": "2022-02-01 21:33:11 UTC",
  "manuscript": "bar",
  "variant": "default",
  "manuscript_path": "examples/bar",
  "config_path": "examples/bar/render-config.json",
  "config_hash_sha256": "1a7de86e951d0d9374cee0dc1152fe781f16db072cb45985c300d4477374bd6e",
  "config_data_version": "2022-01-30 15:42:38 UTC",
  "config_size_bytes": 59,
  "render_config": {
    "name": "the-name-of-the-thing"
  },
  "binder_path": "examples/bar/bind-default.txt",
  "binder_hash_sha256": "38cf0d8e52b3020eb9e750c30998e1759657ad927462621ddd0b706b79a140c5",
  "binder_data_version": "2022-01-30 15:41:15 UTC",
  "binder_size_bytes": 7,
  "binder": [
    "examples/bar/foo.md"
  ]
}
```

### Render

Another variant using environment variables to specify publisher and render root:

```console
$ GENGIVE_PUBLISHER_ROOT=/somewhere/gengive \
 GENGIVE_RENDER_ROOT=/somewhere/gengive gengive render --manuscript bar --target default
Retrieving manuscript folders below /somewhere/gengive ...
- bar
Identifying variants defined for document(bar) ...
- default
Requested rendering document(bar) for target(default) below /somewhere/gengive/render/bar/default/ ...
Binder analysis OK, all files resolve. Sequence of binding will be:
 1: /somewhere/gengive/bar/foo.md
Binding source documents from (bar) for target(default) to /somewhere/gengive/render/bar/default/the-name-of-the-thing.md ...
- Written 37 lines from 1 parts to /somewhere/gengive/render/bar/default/the-name-of-the-thing.md
Writing HTML rendition from (bar) for target(default) to /Usomewhere/gengive/render/bar/default/html/the-name-of-the-thing.html ...
Creating HTML rendition of document(bar) for target(default) below /somewhere/gengive/render/bar/default/html/ ...
Determine set of media assets in use ...
Copying the per conventions 2 media asset folders from source to target ...
Done. Entrypoint is /somewhere/gengive/render/bar/default/html/the-name-of-the-thing.html
```

```console
$ ls -lrt render/bar/default
total 16
drwxr-xr-x  3 ruth  staff    96 30 Jan 16:42 html
-rw-r--r--  1 ruth  staff   365 30 Jan 17:13 the-name-of-the-thing.md
-rw-r--r--  1 ruth  staff  1758 30 Jan 17:13 render-info.json
```

```console
$ cat render/bar/default/render-info.json
{
  "request_parameters": [
    "render",
    "bar",
    "default"
  ],
  "processing_start": "2022-01-30 16:13:25 UTC",
  "manuscript": "bar",
  "variant": "default",
  "manuscript_path": "/somewhere/gengive/bar",
  "config_path": "/somewhere/gengive/bar/render-config.json",
  "config_hash_sha256": "1a7de86e951d0d9374cee0dc1152fe781f16db072cb45985c300d4477374bd6e",
  "config_data_version": "2022-01-30 15:42:38 UTC",
  "config_size_bytes": 59,
  "render_config": {
    "name": "the-name-of-the-thing"
  },
  "binder_path": "/somewhere/gengive/bar/bind-default.txt",
  "binder_hash_sha256": "38cf0d8e52b3020eb9e750c30998e1759657ad927462621ddd0b706b79a140c5",
  "binder_data_version": "2022-01-30 15:41:15 UTC",
  "binder_size_bytes": 7,
  "binder": [
    "/somewhere/gengive/bar/foo.md"
  ],
  "collation_folder": "/somewhere/gengive/render/bar/default",
  "collation_name": "the-name-of-the-thing.md",
  "collation_path": "/somewhere/gengive/render/bar/default/the-name-of-the-thing.md",
  "collation_hash_sha256": "1703ff76265d987223d4b18daabc2b831b7af01b441a01ad28239c58d37b346f",
  "collation_data_version": "2022-01-30 16:13:25 UTC",
  "collation_size_bytes": 365,
  "lines_written": 37,
  "html_folder": "/somewhere/gengive/render/bar/default/html",
  "html_name": "the-name-of-the-thing.html",
  "html_path": "/somewhere/gengive/render/bar/default/html/the-name-of-the-thing.html",
  "html_hash_sha256": "a0fe71f2ee2da036f343b40fa5818fbf17f6ec0db620e425401dccadb74b7d79",
  "html_data_version": "2022-01-30 16:13:25 UTC",
  "html_size_bytes": 2145,
  "asset_descriptions": [],
  "processing_stop": "2022-01-30 16:13:25 UTC",
  "processing_duration_seconds": 0.044616
}
```

```console
$ cat bar/bind-default.txt
foo.md
```

```console
$ cat bar/render-config.json
{
  "default": {
    "name": "the-name-of-the-thing"
  }
}
```

```console
$ cat bar/foo.md
# Heading Wun

We talk from time to time.

- wun
- two
- three

1. again wun
1. two
1. three
1. and four

> a blockquote

!!! note
    Notes are this way

## Subesection

Yes a subsection

```python
print(42)
\```

## A Table Section

| Something | was | here |
|:--------- |:--- |:---- |
| or        | did | not  |

A missing image ![so missed](picture.jpg)

End.

```

```console
$ cat render/bar/default/the-name-of-the-thing.md
# Heading Wun

We talk from time to time.

- wun
- two
- three

1. again wun
1. two
1. three
1. and four

> a blockquote

!!! note
    Notes are this way

## Subesection

Yes a subsection

```python
print(42)
\```

## A Table Section

| Something | was | here |
|:--------- |:--- |:---- |
| or        | did | not  |

A missing image ![so missed](picture.jpg)

End.

```

```console
$ cat render/bar/default/html/the-name-of-the-thing.html
<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="description" content="Some Documents 'the-name-of-the-thing.md'.">
        <meta name="viewport" content="width=device-width, initial-scale=1">
          <style>
            html {font-family: "ITC Franklin Gothic Std Bk Cd", Verdana, Arial, sans-serif;}
            a {color: #0c2d82;}
            b {font-weight: 600;}
            h1 {font-weight: 300; text-transform: capitalize;}
            h2 {font-weight: 200;}
            li {line-height: 1.5;}
            table {table-layout: fixed; width: 90%; background-color: #ffffff; margin: 20px;
              border-collapse: collapse;}
            td, th {word-wrap: break-word; border: solid 1px #666666;}
            th {background-color: #0c2d82; color: #ffffff; font-size: 75%; font-weight: 300;}
            td {vertical-align: top; font-size: 67%; padding: 2px;}
            table caption {font-size: 120%; margin-bottom: 20px;}
            tbody tr:nth-child(odd) {background-color: #dddddd;}
            tbody tr:nth-child(even) {background-color: #ffffff;}
          </style>
        <title>the-name-of-the-thing.md</title>
      </head>
    <body>
    <h1 id="heading-wun">Heading Wun</h1>
<p>We talk from time to time.</p>
<ul>
<li>wun</li>
<li>two</li>
<li>
<p>three</p>
</li>
<li>
<p>again wun</p>
</li>
<li>two</li>
<li>three</li>
<li>and four</li>
</ul>
<blockquote>
<p>a blockquote</p>
</blockquote>
<p>!!! note
    Notes are this way</p>
<h2 id="subesection">Subesection</h2>
<p>Yes a subsection</p>
<div class="codehilite"><pre><span></span><code><span class="nb">print</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
</code></pre></div>

<h2 id="a-table-section">A Table Section</h2>
<table>
<thead>
<tr>
<th align="left">Something</th>
<th align="left">was</th>
<th align="left">here</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">or</td>
<td align="left">did</td>
<td align="left">not</td>
</tr>
</tbody>
</table>
<p>A missing image <img alt="so missed" src="picture.jpg"></p>
<p>End.</p>
    </body>
    </html>

```
