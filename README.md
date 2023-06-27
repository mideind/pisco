# Prompts for Icelandic Corpus (PIsCo)
## Raw format
Each example consists of three separate files:

```
pisco
├── revision-1
│   └── wikihow
│       ├── 1.conversation.md
│       ├── 1.meta.toml
│       └── 1.source.txt
```

Metadata about each example is stored in [TOML format](https://toml.io/en/). The keys are still a bit undefined. But it has at least the following structure:

```toml
url = "https://www.wikihow.com/Find-the-URL-of-a-Website"
comment = "Comment for the example that will be included in the jsonl release"
original_author = "haukurb"  # github profile
reviewers = [
  "haukurb",
]
```

The url and comment may be omitted (i.e. be null).

## Conversation format
We use the same scheme as [StableLM](https://github.com/Stability-AI/StableLM). So our example conversation would be:

```markdown
<|user|>
Hæbb
<|system|>
Sæll vertu! Hvað get ég gert fyrir þig?

Ef þú hefur einhverjar spurningar eða vangaveltur þá mun ég reyna mitt besta til að svara þeim.
<|user|>
Hvað er eiginlega mállíkan?
<|system|>
Mállíkan er eins konar gerð af gervigreind sem skilur, skapar og vinnur á mennsku máli. Það má líta á það sem flókið tölfræðilíkan sem hjálpar tölvunni að skilja mannlegt mál. Mállíkön geta ýmist unnið á rituðu máli, töluðu máli, táknmáli, eða máli á myndrænu formi. Mállíkön eru búin til með því að „þjálfa” það á máldæmum úr risastórum gagnasöfnum, með þeim hætti getur það lært málfræði, hvernig orð tengjast samhengjum sínum og gert þeim kleift mynda setningar sem ná einhverri átt svo það geti leyst ýmis verkefni eins og að þýða texta, gera samantekt úr texta eða svara spurningum.
```

## Revisions and versions
We distinguish between revisions and versions. Versions of the corpus refer to releases. We use revisions to differentiate between iterations of review-refinement, so revision-1 can therefore be quite deficient in terms of grammar, vocabulary, style and fluency.

Even though revision-1 is unrefined, we do require that the source text (if there is any) has been converted into prompt-and-answer format and they must be adequately localized.
