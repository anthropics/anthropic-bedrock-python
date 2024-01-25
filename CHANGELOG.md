# Changelog

## 0.7.0 (2024-01-25)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.6.0...v0.7.0)

### Features

* **client:** enable follow redirects by default ([#131](https://github.com/anthropics/anthropic-bedrock-python/issues/131)) ([aa95ff7](https://github.com/anthropics/anthropic-bedrock-python/commit/aa95ff73344d33025e9a4c090228813f645cd1bf))


### Chores

* **internal:** add internal helpers ([#128](https://github.com/anthropics/anthropic-bedrock-python/issues/128)) ([dedf694](https://github.com/anthropics/anthropic-bedrock-python/commit/dedf694e6c7de5e03e017d1ce7911c15c04a0f04))

## 0.6.0 (2024-01-18)

Full Changelog: [v0.5.9...v0.6.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.9...v0.6.0)

### Features

* **client:** add support for streaming raw responses ([#118](https://github.com/anthropics/anthropic-bedrock-python/issues/118)) ([41a1aa3](https://github.com/anthropics/anthropic-bedrock-python/commit/41a1aa3dc46a6e49dffe312dc33c582046569bc2))


### Bug Fixes

* **ci:** ignore stainless-app edits to release PR title ([#127](https://github.com/anthropics/anthropic-bedrock-python/issues/127)) ([662b250](https://github.com/anthropics/anthropic-bedrock-python/commit/662b250ccd9d5ae93cd7ac0998fd592c0ae8f6e6))


### Chores

* add write_to_file binary helper method ([#120](https://github.com/anthropics/anthropic-bedrock-python/issues/120)) ([7ac6d5b](https://github.com/anthropics/anthropic-bedrock-python/commit/7ac6d5b34d3e690d10c674af9bebfdd3d1736809))
* **client:** improve debug logging for failed requests ([#115](https://github.com/anthropics/anthropic-bedrock-python/issues/115)) ([9a53654](https://github.com/anthropics/anthropic-bedrock-python/commit/9a53654135c2008dc66228b578fc5ed0deb83a99))
* **internal:** fix typing util function ([#121](https://github.com/anthropics/anthropic-bedrock-python/issues/121)) ([78c1927](https://github.com/anthropics/anthropic-bedrock-python/commit/78c19276b618a3f0198588f5f7ca9a46b2ba88f1))
* **internal:** remove redundant client test ([#122](https://github.com/anthropics/anthropic-bedrock-python/issues/122)) ([6403fe4](https://github.com/anthropics/anthropic-bedrock-python/commit/6403fe4ef48a50a205555329399a3bb1a790180b))
* **internal:** share client instances between all tests ([#125](https://github.com/anthropics/anthropic-bedrock-python/issues/125)) ([d9aa8a1](https://github.com/anthropics/anthropic-bedrock-python/commit/d9aa8a1f2377ddfba98c5c11abbd6c82c0e72d3e))
* **internal:** speculative retry-after-ms support ([#123](https://github.com/anthropics/anthropic-bedrock-python/issues/123)) ([e82e62e](https://github.com/anthropics/anthropic-bedrock-python/commit/e82e62eb60597d7ae87d9b154661a21eb552c019))
* **internal:** updates to proxy helper ([#119](https://github.com/anthropics/anthropic-bedrock-python/issues/119)) ([0383e44](https://github.com/anthropics/anthropic-bedrock-python/commit/0383e44e58ed8a41eb1e4ec434e0e58c48f34c39))
* lazy load raw resource class properties ([#124](https://github.com/anthropics/anthropic-bedrock-python/issues/124)) ([dea3b90](https://github.com/anthropics/anthropic-bedrock-python/commit/dea3b90b0ee300bfb6cd07574e80e1eb180a2ca3))


### Documentation

* **readme:** improve api reference ([#117](https://github.com/anthropics/anthropic-bedrock-python/issues/117)) ([f255984](https://github.com/anthropics/anthropic-bedrock-python/commit/f255984201733db377723fba1e22ce3e3e0eec88))

## 0.5.9 (2024-01-08)

Full Changelog: [v0.5.8...v0.5.9](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.8...v0.5.9)

### Bug Fixes

* **client:** correctly use custom http client auth ([#110](https://github.com/anthropics/anthropic-bedrock-python/issues/110)) ([10ae9d4](https://github.com/anthropics/anthropic-bedrock-python/commit/10ae9d4ed6ead49a7f290611f4a14da43cef7c89))


### Chores

* add .keep files for examples and custom code directories ([#114](https://github.com/anthropics/anthropic-bedrock-python/issues/114)) ([de6bd21](https://github.com/anthropics/anthropic-bedrock-python/commit/de6bd219119dec4c324c20a3009b9fdd94af44d1))
* **ci:** run release workflow once per day ([#101](https://github.com/anthropics/anthropic-bedrock-python/issues/101)) ([02e331a](https://github.com/anthropics/anthropic-bedrock-python/commit/02e331ad34bcaaa4ac75000eb25c3e93127ff6d7))
* **internal:** add bin script ([#107](https://github.com/anthropics/anthropic-bedrock-python/issues/107)) ([159d3d1](https://github.com/anthropics/anthropic-bedrock-python/commit/159d3d142cd0edbb63a3dc3a71f46206af699037))
* **internal:** fix typos ([#105](https://github.com/anthropics/anthropic-bedrock-python/issues/105)) ([4364c8e](https://github.com/anthropics/anthropic-bedrock-python/commit/4364c8e0d810698a222396f3c16c2896a99e6ab1))
* **internal:** loosen type var restrictions ([#113](https://github.com/anthropics/anthropic-bedrock-python/issues/113)) ([c7bc3af](https://github.com/anthropics/anthropic-bedrock-python/commit/c7bc3afaa911436ae424a2ccb9bc4a55f7ea20e3))
* **internal:** minor utils restructuring ([#104](https://github.com/anthropics/anthropic-bedrock-python/issues/104)) ([00c3491](https://github.com/anthropics/anthropic-bedrock-python/commit/00c34910663c216ed50d3fd7663ae7fd48239a3e))
* **internal:** replace isort with ruff ([#111](https://github.com/anthropics/anthropic-bedrock-python/issues/111)) ([0193bb6](https://github.com/anthropics/anthropic-bedrock-python/commit/0193bb67d130bffc30f4cd78cd52c08cca50d907))
* **internal:** use ruff instead of black for formatting ([#109](https://github.com/anthropics/anthropic-bedrock-python/issues/109)) ([4bc28b0](https://github.com/anthropics/anthropic-bedrock-python/commit/4bc28b0a739dcb84c4450e3414b7c61cef9405bf))
* **package:** bump minimum typing-extensions to 4.7 ([#106](https://github.com/anthropics/anthropic-bedrock-python/issues/106)) ([50227fd](https://github.com/anthropics/anthropic-bedrock-python/commit/50227fd4931ae7356ef77cbf75b109d7769f4e1d))
* **streaming:** update constructor to use direct client names ([#103](https://github.com/anthropics/anthropic-bedrock-python/issues/103)) ([2d162ef](https://github.com/anthropics/anthropic-bedrock-python/commit/2d162efdb5fcf40603e2e4705a13acc53efa9267))
* use property declarations for resource members ([#112](https://github.com/anthropics/anthropic-bedrock-python/issues/112)) ([0704047](https://github.com/anthropics/anthropic-bedrock-python/commit/070404797293fef52350ff1025cf7dd20e11cc13))

## 0.5.8 (2023-12-12)

Full Changelog: [v0.5.7...v0.5.8](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.7...v0.5.8)

### Bug Fixes

* avoid leaking memory when Client.with_options is used ([#97](https://github.com/anthropics/anthropic-bedrock-python/issues/97)) ([5d33836](https://github.com/anthropics/anthropic-bedrock-python/commit/5d338361ce8076ffa6fe6e3a4acf1d56eaf63496))
* **errors:** properly assign APIError.body ([#96](https://github.com/anthropics/anthropic-bedrock-python/issues/96)) ([e81848f](https://github.com/anthropics/anthropic-bedrock-python/commit/e81848f4d6b2155947a865d2b49cd9049de24591))


### Chores

* **internal:** enable more lint rules ([#94](https://github.com/anthropics/anthropic-bedrock-python/issues/94)) ([89ecfb9](https://github.com/anthropics/anthropic-bedrock-python/commit/89ecfb99fe562af7a77df5b529ac30355ee4b18f))
* **internal:** reformat imports ([#91](https://github.com/anthropics/anthropic-bedrock-python/issues/91)) ([dbe9399](https://github.com/anthropics/anthropic-bedrock-python/commit/dbe9399fc7e383e2c99bd786697a5fdb58e9bb81))
* **internal:** reformat imports ([#93](https://github.com/anthropics/anthropic-bedrock-python/issues/93)) ([df2fd4c](https://github.com/anthropics/anthropic-bedrock-python/commit/df2fd4c3131bcff7ddd6a67b89932d47ac0c7628))
* **internal:** update formatting ([#92](https://github.com/anthropics/anthropic-bedrock-python/issues/92)) ([df7365f](https://github.com/anthropics/anthropic-bedrock-python/commit/df7365f35a2c2978229eecc2b61a833a1dd82e52))
* **internal:** update test examples ([#98](https://github.com/anthropics/anthropic-bedrock-python/issues/98)) ([efffacd](https://github.com/anthropics/anthropic-bedrock-python/commit/efffacd9ee0083242fcaeb97b589f1ab9b15aa5e))


### Refactors

* **client:** simplify cleanup ([#99](https://github.com/anthropics/anthropic-bedrock-python/issues/99)) ([9ba7039](https://github.com/anthropics/anthropic-bedrock-python/commit/9ba70398e00400bf4a9630c47845366e32916ad8))
* simplify internal error handling ([#100](https://github.com/anthropics/anthropic-bedrock-python/issues/100)) ([1ecff82](https://github.com/anthropics/anthropic-bedrock-python/commit/1ecff82840229eefe36542dee05c5d9e5947f82b))

## 0.5.7 (2023-12-06)

Full Changelog: [v0.5.6...v0.5.7](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.6...v0.5.7)

### Bug Fixes

* bump default request timeout to 10min to match documentation ([#88](https://github.com/anthropics/anthropic-bedrock-python/issues/88)) ([fc85322](https://github.com/anthropics/anthropic-bedrock-python/commit/fc8532218cf327b689718e96e30dc6de201c3eb2))
* **client:** correct base_url setter implementation ([#84](https://github.com/anthropics/anthropic-bedrock-python/issues/84)) ([6983847](https://github.com/anthropics/anthropic-bedrock-python/commit/698384793dad3d202a04498c67df5672037a5ada))
* **client:** ensure retried requests are closed ([#80](https://github.com/anthropics/anthropic-bedrock-python/issues/80)) ([3f28ec8](https://github.com/anthropics/anthropic-bedrock-python/commit/3f28ec864b48f694976f4cc69ee693c7d7082abf))


### Chores

* **internal:** remove unused file ([#83](https://github.com/anthropics/anthropic-bedrock-python/issues/83)) ([aa0ed40](https://github.com/anthropics/anthropic-bedrock-python/commit/aa0ed406abfad95df6d51e050402f8448dbdbdaa))
* **internal:** replace string concatenation with f-strings ([#82](https://github.com/anthropics/anthropic-bedrock-python/issues/82)) ([e3545db](https://github.com/anthropics/anthropic-bedrock-python/commit/e3545db53fa8dbeb8b302c3072e13c6a1f020533))
* **package:** lift anyio v4 restriction ([#85](https://github.com/anthropics/anthropic-bedrock-python/issues/85)) ([8879c77](https://github.com/anthropics/anthropic-bedrock-python/commit/8879c777da8d4d1cc5de7e5d7ffcabd442e61591))

## 0.5.6 (2023-11-29)

Full Changelog: [v0.5.5...v0.5.6](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.5...v0.5.6)

### Chores

* **deps:** bump mypy to v1.7.1 ([#76](https://github.com/anthropics/anthropic-bedrock-python/issues/76)) ([3fdd760](https://github.com/anthropics/anthropic-bedrock-python/commit/3fdd7607c7ab1e3a8b9172b4a8cac7963f35e6b5))
* **internal:** add tests for proxy change ([#79](https://github.com/anthropics/anthropic-bedrock-python/issues/79)) ([7fec890](https://github.com/anthropics/anthropic-bedrock-python/commit/7fec89000cb5d779ebe973be7ad13e511dddb00e))
* **internal:** updates to proxy helper ([#78](https://github.com/anthropics/anthropic-bedrock-python/issues/78)) ([ff727ff](https://github.com/anthropics/anthropic-bedrock-python/commit/ff727ff8eee83a102e6fdd601a911f98f4818244))

## 0.5.5 (2023-11-24)

Full Changelog: [v0.5.4...v0.5.5](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.4...v0.5.5)

### Chores

* **internal:** revert recent options change ([#73](https://github.com/anthropics/anthropic-bedrock-python/issues/73)) ([ddff306](https://github.com/anthropics/anthropic-bedrock-python/commit/ddff3062dde2e0a40856a7fb3d892a41ac19c09e))
* **internal:** send more detailed x-stainless headers ([#75](https://github.com/anthropics/anthropic-bedrock-python/issues/75)) ([654604e](https://github.com/anthropics/anthropic-bedrock-python/commit/654604eb04a6e85b402c4c3712a26fa738582ff6))

## 0.5.4 (2023-11-23)

Full Changelog: [v0.5.3...v0.5.4](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.3...v0.5.4)

### Chores

* **internal:** options updates ([#71](https://github.com/anthropics/anthropic-bedrock-python/issues/71)) ([6db76e8](https://github.com/anthropics/anthropic-bedrock-python/commit/6db76e8a08aec42e5236320e5c9063f4b393289a))

## 0.5.3 (2023-11-21)

Full Changelog: [v0.5.2...v0.5.3](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.2...v0.5.3)

### Bug Fixes

* **client:** attempt to parse unknown json content types ([#67](https://github.com/anthropics/anthropic-bedrock-python/issues/67)) ([b9a9ef4](https://github.com/anthropics/anthropic-bedrock-python/commit/b9a9ef45c2212f8f33378cfd52f2dca8c50c5547))


### Chores

* **client:** improve copy method ([#69](https://github.com/anthropics/anthropic-bedrock-python/issues/69)) ([f5294f2](https://github.com/anthropics/anthropic-bedrock-python/commit/f5294f21be89771e5ee0b6c4713052e50143fffa))
* **package:** add license classifier metadata ([#70](https://github.com/anthropics/anthropic-bedrock-python/issues/70)) ([c34cb2a](https://github.com/anthropics/anthropic-bedrock-python/commit/c34cb2ab8356abca2bb0b2ad4e83fa89900d3546))

## 0.5.2 (2023-11-17)

Full Changelog: [v0.5.1...v0.5.2](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.1...v0.5.2)

### Chores

* **internal:** update type hint for helper function ([#65](https://github.com/anthropics/anthropic-bedrock-python/issues/65)) ([19a3b94](https://github.com/anthropics/anthropic-bedrock-python/commit/19a3b9412d66b46c0e004221a1000a2109f861f0))

## 0.5.1 (2023-11-16)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.5.0...v0.5.1)

### Documentation

* **readme:** minor updates ([#63](https://github.com/anthropics/anthropic-bedrock-python/issues/63)) ([cb88f20](https://github.com/anthropics/anthropic-bedrock-python/commit/cb88f20313433ba7a6f68fc81c1e81f5670ed6e7))

## 0.5.0 (2023-11-15)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.4.0...v0.5.0)

### Features

* **client:** support passing chunk size for binary responses ([#52](https://github.com/anthropics/anthropic-bedrock-python/issues/52)) ([e4082c9](https://github.com/anthropics/anthropic-bedrock-python/commit/e4082c9a2f7b7f48153623a36ff013d23e977b4c))
* **client:** support passing httpx.Timeout to method timeout argument ([#47](https://github.com/anthropics/anthropic-bedrock-python/issues/47)) ([e01b122](https://github.com/anthropics/anthropic-bedrock-python/commit/e01b122d2abac7005439ad258e69636f2e1b5082))
* **client:** support reading the base url from an env variable ([#62](https://github.com/anthropics/anthropic-bedrock-python/issues/62)) ([75ad959](https://github.com/anthropics/anthropic-bedrock-python/commit/75ad959130819ebe65d53755870198c755bd1a53))


### Bug Fixes

* **client:** retry if SSLWantReadError occurs in the async client ([#57](https://github.com/anthropics/anthropic-bedrock-python/issues/57)) ([f00c6db](https://github.com/anthropics/anthropic-bedrock-python/commit/f00c6dbc25da426d05adf2013843b7911bc9df49))
* **client:** serialise pydantic v1 default fields correctly in params ([#56](https://github.com/anthropics/anthropic-bedrock-python/issues/56)) ([5bf701b](https://github.com/anthropics/anthropic-bedrock-python/commit/5bf701bbdde40bd50a3756093e45da6fedd21ada))
* **models:** mark unknown fields as set in pydantic v1 ([#55](https://github.com/anthropics/anthropic-bedrock-python/issues/55)) ([2c1b0b1](https://github.com/anthropics/anthropic-bedrock-python/commit/2c1b0b12b6e5c41324f8a68f4698c3012861315c))


### Chores

* **docs:** fix github links ([#50](https://github.com/anthropics/anthropic-bedrock-python/issues/50)) ([08b0b96](https://github.com/anthropics/anthropic-bedrock-python/commit/08b0b96adb225b2affd53930aedfc575f9b613fc))
* **internal:** base client updates ([#54](https://github.com/anthropics/anthropic-bedrock-python/issues/54)) ([9cf0e41](https://github.com/anthropics/anthropic-bedrock-python/commit/9cf0e4186cf7499709060f8a543bb458a8b547d2))
* **internal:** fix devcontainer interpeter path ([#59](https://github.com/anthropics/anthropic-bedrock-python/issues/59)) ([2a5d3f0](https://github.com/anthropics/anthropic-bedrock-python/commit/2a5d3f0ee7997a9a16a99f1b3fe08bc298c6a404))
* **internal:** fix some typos ([#49](https://github.com/anthropics/anthropic-bedrock-python/issues/49)) ([e1e9ce9](https://github.com/anthropics/anthropic-bedrock-python/commit/e1e9ce96be9f6c7848bc0087a5f48f8851516ed3))
* **internal:** fix typo in NotGiven docstring ([#58](https://github.com/anthropics/anthropic-bedrock-python/issues/58)) ([3956ed9](https://github.com/anthropics/anthropic-bedrock-python/commit/3956ed9744c8b9b58f6252f81c09a87f87e332ff))
* **internal:** improve github devcontainer setup ([#51](https://github.com/anthropics/anthropic-bedrock-python/issues/51)) ([8afa9d8](https://github.com/anthropics/anthropic-bedrock-python/commit/8afa9d82390922d015df7ae31350e3593913e4d2))


### Documentation

* fix code comment typo ([#60](https://github.com/anthropics/anthropic-bedrock-python/issues/60)) ([6d7636a](https://github.com/anthropics/anthropic-bedrock-python/commit/6d7636a6b982f67814548ad0f0af90767d427a30))
* reword package description ([#53](https://github.com/anthropics/anthropic-bedrock-python/issues/53)) ([e6d3666](https://github.com/anthropics/anthropic-bedrock-python/commit/e6d3666e26f16ffd3cb1d45bd8caf7476bd38b36))

## 0.4.0 (2023-11-06)

Full Changelog: [v0.3.1...v0.4.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.3.1...v0.4.0)

### Features

* **client:** allow binary returns ([#41](https://github.com/anthropics/anthropic-bedrock-python/issues/41)) ([bdc3240](https://github.com/anthropics/anthropic-bedrock-python/commit/bdc3240984f4826fd5a50ce9b7857b65e398ef04))
* **client:** support accessing raw response objects ([#34](https://github.com/anthropics/anthropic-bedrock-python/issues/34)) ([1833b84](https://github.com/anthropics/anthropic-bedrock-python/commit/1833b8487950a2628b87cac62813b3feadad7261))
* **client:** support passing BaseModels to request params at runtime ([#42](https://github.com/anthropics/anthropic-bedrock-python/issues/42)) ([b2f3ac5](https://github.com/anthropics/anthropic-bedrock-python/commit/b2f3ac5af7dd87d24cdb291c25f2cdfcbf916e59))
* **github:** include a devcontainer setup ([#40](https://github.com/anthropics/anthropic-bedrock-python/issues/40)) ([8a74a91](https://github.com/anthropics/anthropic-bedrock-python/commit/8a74a9189761979b93ba9bcfb1ac4a36b1f858ba))
* **package:** add classifiers ([#38](https://github.com/anthropics/anthropic-bedrock-python/issues/38)) ([6670b3d](https://github.com/anthropics/anthropic-bedrock-python/commit/6670b3daf849498a5937d74ca4a894d54767e28d))


### Bug Fixes

* **binaries:** don't synchronously block in astream_to_file ([#43](https://github.com/anthropics/anthropic-bedrock-python/issues/43)) ([0ec53cd](https://github.com/anthropics/anthropic-bedrock-python/commit/0ec53cdfcdfd0ba63725233a4dfe88608eaaa22e))
* prevent TypeError in Python 3.8 (ABC is not subscriptable) ([#46](https://github.com/anthropics/anthropic-bedrock-python/issues/46)) ([a459837](https://github.com/anthropics/anthropic-bedrock-python/commit/a4598370b3949b10099377555c3cbb14ca222e75))


### Chores

* **internal:** minor restructuring of base client ([#37](https://github.com/anthropics/anthropic-bedrock-python/issues/37)) ([e3550c9](https://github.com/anthropics/anthropic-bedrock-python/commit/e3550c97d898c2049ffe067fbfa4ff6025e1d03d))
* **internal:** remove unused int/float conversion ([#45](https://github.com/anthropics/anthropic-bedrock-python/issues/45)) ([7021d09](https://github.com/anthropics/anthropic-bedrock-python/commit/7021d098706d88a7a62b80f6ca9a0d66219e757f))


### Documentation

* **api:** improve method signatures for named path params ([#44](https://github.com/anthropics/anthropic-bedrock-python/issues/44)) ([a9d8bd3](https://github.com/anthropics/anthropic-bedrock-python/commit/a9d8bd392bb5f465dfd760a58f6fd8e3ab6e07cb))
* fix github links ([#39](https://github.com/anthropics/anthropic-bedrock-python/issues/39)) ([c1ad694](https://github.com/anthropics/anthropic-bedrock-python/commit/c1ad69475e65788cf5524a4a2b3df6a858176f95))

## 0.3.1 (2023-10-26)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.3.0...v0.3.1)

### Chores

* **internal:** require explicit overrides ([#32](https://github.com/anthropics/anthropic-bedrock-python/issues/32)) ([115d525](https://github.com/anthropics/anthropic-bedrock-python/commit/115d525202d0e3c04b604c597b496da7013149ea))

## 0.3.0 (2023-10-25)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.2.1...v0.3.0)

### Features

* **client:** adjust retry behavior to be exponential backoff ([#26](https://github.com/anthropics/anthropic-bedrock-python/issues/26)) ([c231377](https://github.com/anthropics/anthropic-bedrock-python/commit/c231377ea175f6dba3376d8dfb2e236ac51d1547))
* **client:** improve file upload types ([#25](https://github.com/anthropics/anthropic-bedrock-python/issues/25)) ([eb651e3](https://github.com/anthropics/anthropic-bedrock-python/commit/eb651e349b956f19f328421a3b55b10860ab53d3))


### Documentation

* improve to dictionary example ([#28](https://github.com/anthropics/anthropic-bedrock-python/issues/28)) ([8c226c0](https://github.com/anthropics/anthropic-bedrock-python/commit/8c226c01eb808e95a2e562858690b140b22ad893))

## 0.2.1 (2023-10-20)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.2.0...v0.2.1)

### Chores

* **internal:** bump mypy ([#24](https://github.com/anthropics/anthropic-bedrock-python/issues/24)) ([87e57df](https://github.com/anthropics/anthropic-bedrock-python/commit/87e57df17f9811118d85c1ff6dd963a1aed08262))
* **internal:** bump pyright ([#23](https://github.com/anthropics/anthropic-bedrock-python/issues/23)) ([325a219](https://github.com/anthropics/anthropic-bedrock-python/commit/325a2192c8f70ec7dc56390df7e743b7dbd3bfcd))
* **internal:** update gitignore ([#20](https://github.com/anthropics/anthropic-bedrock-python/issues/20)) ([17fb6c1](https://github.com/anthropics/anthropic-bedrock-python/commit/17fb6c121eaf144b3ee448eea78bd55cbd3c1253))

## 0.2.0 (2023-10-18)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.1.1...v0.2.0)

### Features

* **client:** support passing httpx.URL instances to base_url ([#17](https://github.com/anthropics/anthropic-bedrock-python/issues/17)) ([ab60451](https://github.com/anthropics/anthropic-bedrock-python/commit/ab60451e4f104e7739ce5e483ebfe40da9ea0d3e))


### Chores

* **internal:** improve publish script ([#16](https://github.com/anthropics/anthropic-bedrock-python/issues/16)) ([db74296](https://github.com/anthropics/anthropic-bedrock-python/commit/db74296def9f9f9e8c13ef4c12bf0d8e3715c209))
* **internal:** migrate from Poetry to Rye ([#14](https://github.com/anthropics/anthropic-bedrock-python/issues/14)) ([0d687d5](https://github.com/anthropics/anthropic-bedrock-python/commit/0d687d53670e3ebfc1f87f6160d46777ab249475))
* **internal:** update gitignore ([#19](https://github.com/anthropics/anthropic-bedrock-python/issues/19)) ([a952733](https://github.com/anthropics/anthropic-bedrock-python/commit/a952733553b70bdbabc0f6a09b5d5a5578ac50ca))

## 0.1.1 (2023-10-16)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.1.0...v0.1.1)

### Bug Fixes

* **client:** accept io.IOBase instances in file params ([#11](https://github.com/anthropics/anthropic-bedrock-python/issues/11)) ([67a96fe](https://github.com/anthropics/anthropic-bedrock-python/commit/67a96fe42022d4406c1eac96b4d3eae52ca2a6db))
* **streaming:** add additional overload for ambiguous stream param ([#6](https://github.com/anthropics/anthropic-bedrock-python/issues/6)) ([c697b25](https://github.com/anthropics/anthropic-bedrock-python/commit/c697b25f7c62b455bc865a06946a4fdd57f37f73))


### Chores

* add case insensitive get header function ([#3](https://github.com/anthropics/anthropic-bedrock-python/issues/3)) ([684ecb5](https://github.com/anthropics/anthropic-bedrock-python/commit/684ecb5cf6e77e759a3bad6eb2157894727e0e00))
* **internal:** cleanup some redundant code ([#7](https://github.com/anthropics/anthropic-bedrock-python/issues/7)) ([13a7e4f](https://github.com/anthropics/anthropic-bedrock-python/commit/13a7e4f5b4afc12a4a35547510ea074783ccf01a))
* **internal:** enable lint rule ([#9](https://github.com/anthropics/anthropic-bedrock-python/issues/9)) ([583cd6a](https://github.com/anthropics/anthropic-bedrock-python/commit/583cd6a8048b2798839792ba5809ea014d4a8ce4))
* update comment ([#5](https://github.com/anthropics/anthropic-bedrock-python/issues/5)) ([0b78464](https://github.com/anthropics/anthropic-bedrock-python/commit/0b78464abbd838b134e947d7a39a2a569d83a1f8))


### Documentation

* organisation -&gt; organization (UK to US English) ([#13](https://github.com/anthropics/anthropic-bedrock-python/issues/13)) ([8492991](https://github.com/anthropics/anthropic-bedrock-python/commit/849299143898bfda627dfa940eed43e09a7dfcc7))

## 0.1.0 (2023-10-12)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.0.1...v0.1.0)

### Features

* **init:** initial commit ([#1](https://github.com/anthropics/anthropic-bedrock-python/issues/1)) ([6fb2922](https://github.com/anthropics/anthropic-bedrock-python/commit/6fb29226c2fbf2c4303746a6f9e13ba48600e0e4))
