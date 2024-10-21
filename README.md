# Text to speech for docetl

Example config (using [docetl-conversation](https://github.com/redhog/docetl-conversation) to generate messages to speak):

```yaml
operations:
- name: conversation
  type: conversation
  length: 6
  names:
    - Alice
    - Bob

- name: speaker
  type: speaker
  speaker_key: speaker
  text_key: text
  output_dir: ./
  output_format: mp3
  voices:
    Alice: melotts:EN-US
    Bob: openai:alloy
```

Output:

```json
[
  {
    "speaker": "Alice",
    "text": "What are some key rights that purchasers should be aware of when making a purchase?",
    "concept": "Rights of Purchasers",
    "sound": "./0.mp3"
  },
  {
    "speaker": "Bob",
    "text": "When making a purchase, purchasers should be aware of their right to receive the product as described, the right to a refund or replacement for faulty products, and the right to consumer protection laws. How does market functionality impact these rights?",
    "concept": "Market Functionality",
    "sound": "./1.mp3"
  },
  {
    "speaker": "Alice",
    "text": "How does the functionality of rental markets influence the rights of purchasers in terms of product descriptions, refunds, and consumer protection laws?",
    "concept": "Rental Markets",
    "sound": "./2.mp3"
  },
  {
    "speaker": "Bob",
    "text": "The functionality of rental markets can influence purchasers' rights by providing more flexibility in product descriptions, offering different refund policies based on rental terms, and potentially impacting consumer protection laws based on ownership versus rental agreements. How do you think ownership versus rental dynamics play a role in consumer rights in rental markets?",
    "concept": "Ownership vs. Rental",
    "sound": "./3.mp3"
  },
  {
    "speaker": "Alice",
    "text": "The dynamics of ownership versus rental can impact consumer rights in rental markets by defining the level of control and responsibility consumers have over the products they are using. Additionally, licensing in rental markets can influence consumer rights by restricting the rights of third parties not involved in the agreements, potentially limiting competition and consumer choices.",
    "concept": "Licensing",
    "sound": "./4.mp3"
  }
]
```
