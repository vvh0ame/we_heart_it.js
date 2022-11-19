import requests

class WeHeartIt:
    def __init__(self) -> None:
        self.api = "https://api.weheartit.com"
        self.headers = {
            "user-agent": "okhttp/3.14.9",
            "x-weheartit-client": "os: 'Android', sdkVersion: '25', device: 'ASUS_Z01QD', appVersion: '9.0.1.RC-GP-Free(21892) (21892)'"
        }
        self.user_id = None
        self.access_token = None

    def register(
            self,
            email: str,
            password: str,
            username: str,
            signature: str,
            is_private: bool = False) -> dict:
        data = {
            "signature": signature,
            "user": {
                "age_verified": True,
                "email": email,
                "name": username,
                "password": password,
                "private_account": is_private,
                "username": username
            }
        }
        return requests.post(
            f"{self.api}/api/v2/users",
            json=data,
            headers=self.headers).json()

    def login(
            self,
            username: str,
            password: str,
            signature: str) -> dict:
        data = {
            "username": username,
            "password": password,
            "signature": signature,
            "grant_type": "password"
        }
        response = requests.post(
            f"{self.api}/oauth/token",
            json=data,
            headers=self.headers).json()
        if "access_token" in response:
            self.access_token = response["access_token"]
            self.headers["authorization"] = f"Bearer {self.access_token}"
            self.user_id = self.get_current_user()["id"]
        return response

    def login_with_access_token(self, access_token: str) -> dict:
        self.access_token = access_token
        self.headers["authorization"] = f"Bearer {self.access_token}"
        response = self.get_current_user()
        self.user_id = response["id"]
        return response

    def get_user_identities(self, email: str) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users/identities?id={email}",
            headers=self.headers).json()

    def get_current_user(self) -> dict:
        return requests.get(
            f"{self.api}/api/v2/user",
            headers=self.headers).json()

    def get_alerts(self) -> dict:
        return requests.get(
            f"{self.api}/api/v2/user/alerts",
            headers=self.headers).json()

    def get_purchases(self) -> dict:
        return requests.get(
            f"{self.api}/api/v2/user/purchases",
            headers=self.headers).json()

    def search_suggestions(self, query: str) -> dict:
        return requests.get(
            f"{self.api}/api/v2/search/suggestions?query=&popular=1",
            headers=self.headers).json()

    def get_channels(self) -> dict:
        return requests.get(
            f"{self.api}/api/v2/user/channels",
            headers=self.headers).json()

    def get_collections(self, include: str, after: int = None) -> dict:
        url = f"{self.api}/api/v2/collections?include={include}"
        if after:
            url += f"&after={after}"
        return requests.get(
            url, headers=self.headers).json()

    def get_dashboard(
            self,
            include: str = "promoted,promoted_cta,colors,following_status,actions,video,featured_post,reaction_counts",
            limit: int = 10,
            before: int = None) -> dict:
        url =  f"{self.api}/api/v2/user/dashboard/grouped?include={include}&limit={limit}"
        if before:
            url += f"&before={before}"
        return requests.get(
            url, headers=self.headers).json()

    def block_user(self, user_id: int) -> dict:
        data = {
            "user_id": user_id
        }
        return requests.post(
            f"{self.api}/api/v2/user/block_user",
            json=data,
            headers=self.headers).json()

    def unblock_user(self, user_id: int) -> dict:
        data = {
            "user_id": user_id
        }
        return requests.post(
            f"{self.api}/api/v2/user/unblock_user",
            json=data,
            headers=self.headers).json()

    def start_conversation(
            self,
            user_id: [str, list],
            message: str) -> dict:
        if isinstance(user_id, str) -> dict:
            user_ids = [user_id]
        elif isinstance(user_id, list) -> dict:
            user_ids = user_id
        data = {
            "postcard": {
                "message": message,
                "recipient_ids": user_ids
            }
        }
        return requests.post(
            f"{self.api}/api/v2/inbox/conversations",
            json=data,
            headers=self.headers).json()

    def get_blocked_contacts(self) -> dict:
        return requests.get(
            f"{self.api}/api/v2/user/blocked_contacts",
            headers=self.headers).json()

    def get_inspirations(
            self,
            include: str = "colors",
            popular: int = 0,
            offset: int = 75) -> dict:
        return requests.get(
            f"{self.api}/api/v2/inspirations?include={include}&popular={popular}&next_offset={offset}&format=json",
            headers=self.headers).json()

    def get_channel_info(self, channel_id: int) -> dict:
        return requests.get(
            f"{self.api}/api/v2/inspirations/{channel_id}/channel_info",
            headers=self.headers).json()

    def get_channel_articles(self, channel_id: int) -> dict:
        return requests.get(
            f"{self.api}/api/v2/articles/channel/{channel_id}",
            headers=self.headers).json()

    def follow_channel(self, channel_id: int) -> dict:
        return requests.put(
            f"{self.api}/api/v2/inspirations/{channel_id}/join",
            headers=self.headers).json()

    def unfollow_channel(self, channel_id: int) -> dict:
        return requests.put(
            f"{self.api}/api/v2/inspirations/{channel_id}/leave",
            headers=self.headers).json()

    def get_user_info(self, user_id: int) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users/{user_id}",
            headers=self.headers).json()

    def get_user_uploads(
            self,
            user_id: int,
            include: str = "user",
            media_type: str = "article",
            limit: int = 25) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users/{user_id}/uploads?include={include}&media_type={media_type}&limit={limit}",
            headers=self.headers).json()

    def get_user_followers(
            self,
            user_id: int,
            include: str = "recent_hearts",
            page: int = 1) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users/{user_id}/followers?include={include}&page={page}",
            headers=self.headers).json()

    def get_user_followings(
            self,
            user_id: int,
            include: str = "recent_hearts",
            page: int = 1) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users/{user_id}/following?include={include}&page={page}",
            headers=self.headers).json()

    def get_conversation(
            self,
            user_id: int,
            include: str = "colors,promoted,promoted_cta,video,actions",
            mark_as_read: int = 1) -> dict:
        return requests.get(
            f"{self.api}/api/v2/inbox/conversations/{user_id}_{self.user_id}/postcards?include={include}&mark_as_read={mark_as_read}",
            headers=self.headers).json()

    def get_promoted_topics(self) -> dict:
        return requests.get(
            f"{self.api}/api/v2/promoted_topics",
            headers=self.headers).json()

    def get_notifications(self, mark_as_read: bool = False) -> dict:
        return requests.get(
            f"{self.api}/api/v2/notifications?mark_as_read={mark_as_read}",
            headers=self.headers).json()

    def get_conversations(self) -> dict:
        return requests.get(
            F"{self.api}/api/v2/inbox/conversations",
            headers=self.headers).json()

    def get_users_list(
            self,
            include: str = "following_status,recent_hearts",
            limit: int = 25) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users?include={include}&recent_hearts_limit={limit}",
            headers=self.headers).json()

    def recover_account(self, email: str) -> dict:
        data = {
            "email": email
        }
        return requests.post(
            f"{self.api}/api/v2/recover_accounts",
            json=data,
            headers=self.headers).json()

    def edit_profile(
            self,
            name: str = None,
            username: str = None,
            bio: str = None,
            location: str = None,
            link: str = None,
            email: str = None,
            is_public: bool = True,
            is_findable: bool = True) -> dict:
        data = self.get_current_user()
        if name:
            data["name"] = name
        if username:
            data["username"] = username
        if bio:
            data["bio"] = bio
        if location:
            data["location"] = location
        if link:
            data["link"] = link
        if email:
            data["email"] = email
        if is_public:
            data["settings"]["privacy"]["public"] = is_public
        if is_findable:
            data["settings"]["privacy"]["findable"] = is_findable
        return requests.put(
            f"{self.api}/api/v2/user",
            json=data,
            headers=self.headers).json()

    def get_user_entries(self, user_id: int) -> dict:
        return requests.get(
            f"{self.api}/api/v2/users/{user_id}/entries",
            headers=self.headers).json()

    def delete_account(self) -> dict:
        return requests.delete(
            f"{self.api}/api/v2/user?delete_entries=True",
            headers=self.headers).json()
