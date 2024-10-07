class WeHeartIt {
	constructor() {
		this.api = "https://api.weheartit.com"
		this.headers = {
			"User-Agent": "okhttp/3.14.9",
            "x-weheartit-client": "os: 'Android', sdkVersion: '25', device: 'ASUS_Z01QD', appVersion: '9.0.1.RC-GP-Free(21892) (21892)'"
		}
	}

	async register(email, password, userName, signature, isPrivate = false) {
		const response = await fetch(
			`${this.api}/api/v2/users`, {
				method: "POST",
				body: JSON.stringify({
					signature: signature,
					user: {
						age_verified: true,
						email: email,
						name: userName,
						password: password,
						private_account: isPrivate,
						username: userName
					}
				}),
				headers: this.headers
			})
		return response.json()
	}

	async login(username, password, signature) {
		const response = await fetch(
			`${this.api}/oauth/token`, {
				method: "POST",
				body: JSON.stringify({
					username: userName,
					password: password,
					signature: signature,
					grant_type: "password"
				}),
				headers: this.headers
			})
		const data = await response.json()
		this.accessToken = data.access_token
		this.headers["Authorization"] = `Bearer ${this.accessToken}`
		const accountData = await this.getAccountInfo()
		this.userId = accountData.id
		return data
	}

	async getAccountInfo() {
		const response = await fetch(
			`${this.api}/api/v2/user`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAlerts() {
		const response = await fetch(
			`${this.api}/api/v2/user/alerts`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPurchases() {
		const response = await fetch(
			`${this.api}/api/v2/user/purchases`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getChannels() {
		const response = await fetch(
			`${this.api}/api/v2/user/channels`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async searchSuggestions(query) {
		const response = await fetch(
			`${this.api}/api/v2/search/suggestions?query=${query}&popular=1`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCollections(include, after = null) {
		let url = `${this.api}/api/v2/collections?include=${include}`
		if (after) {
			url += `&after=${after}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getDashboard(include = "promoted,promoted_cta,colors,following_status,actions,video,featured_post,reaction_counts", limit = 10, before = null) {
		let url = `${this.api}/api/v2/user/dashboard/grouped?include=${include}&limit=${limit}`
		if (before) {
			url += `&before=${before}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async blockUser(userId) {
		const response = await fetch(
			`${this.api}/api/v2/user/block_user`, {
				method: "GET",
				body: JSON.stringify({
					user_id: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async unblockUser(userId) {
		const response = await fetch(
			`${this.api}/api/v2/user/unblock_user`, {
				method: "GET",
				body: JSON.stringify({
					user_id: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getInspirations(include = "colors", popular = 0, offset = 75) {
		const response = await fetch(
			`${this.api}/api/v2/inspirations?include=${include}&popular=${popular}&next_offset=${offset}&format=json`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getChannelInfo(channelId) {
		const response = await fetch(
			`${this.api}/api/v2/inspirations/${channelId}/channel_info`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getChannelArticles(channelId) {
		const response = await fetch(
			`${this.api}/api/v2/articles/${channelId}/channel_info`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async followChannel(channelId) {
		const response = await fetch(
			`${this.api}/api/v2/inspirations/${channelId}/join`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async unfollowChannel(channelId) {
		const response = await fetch(
			`${this.api}/api/v2/inspirations/${channelId}/leave`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async getUserInfo(userId) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserUploads(userId, include = "user", mediaType = "article", limit = 25) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/uploads?include=${include}&media_type=${mediaType}&limit=${limit}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserFollowers(userId, include = "recent_hearts", page = 1) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/followers?include=${include}&page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserFollowings(userId, include = "recent_hearts", page = 1) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/following?include=${include}&page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getConversation(userId, include = "colors,promoted,promoted_cta,video,actions", markAsRead = 1) {
		const response = await fetch(
			`${this.api}/inbox/conversations/${userId}_${this.userId}/postcards?include=${include}&mark_as_read=${markAsRead}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPromotedTopics() {
		const response = await fetch(
			`${this.api}/api/v2/promoted_topics`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getNotifications() {
		const response = await fetch(
			`${this.api}/api/v2/notifications?mark_as_read=false`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getConversations() {
		const response = await fetch(
			`${this.api}/api/v2/inbox/conversations`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUsers(include = "following_status,recent_hearts", limit = 25) {
		const response = await fetch(
			`${this.api}/api/v2/users?include=${include}&recent_hearts_limit=${limit}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

}

module.exports = {WeHeartIt}
