# we_heart_it.js
Mobile-API for [weheartit](https://play.google.com/store/apps/details?id=com.weheartit) social network

## Example
```JavaScript
async function main() {
	const { WeHeartIt } = require("./we_heart_it.js")
	const weHeartIt = new WeHeartIt()
  await weHeartIt.login("username", "password", "signature")
}

main()
```
