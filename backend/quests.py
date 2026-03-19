import random

# ------------------------------------------------------------
# CATEGORY: Phishing (30)
# ------------------------------------------------------------
phishing = [
    {"question": "Which email characteristic most suggests phishing?",
     "options": [
         "An unexpected urgent request for login credentials",
         "A long friendly newsletter you subscribed to",
         "A known contact sending their normal daily message",
         "A system maintenance notification from your IT team"
     ],
     "correct": 0,
     "explain": "Phishing often requests credentials urgently to trick you into acting without verification."},

    {"question": "What should you do before clicking a link in a suspicious email?",
     "options": [
         "Hover to inspect the actual URL or check the sender through official channels",
         "Click it right away so the page loads faster",
         "Reply with your password to be helpful",
         "Forward it to all your contacts"
     ],
     "correct": 0,
     "explain": "Hovering reveals the link target; verify sender identity through separate trusted channels."},

    {"question": "Why do phishing messages often create a sense of urgency?",
     "options": [
         "To encourage careful research",
         "To make victims act impulsively and bypass checks",
         "To improve the email format",
         "To increase the sender's reputation"
     ],
     "correct": 1,
     "explain": "Urgency reduces deliberation and increases the chance of impulsive mistakes."},

    {"question": "Which of these is a good sign the email might be legitimate?",
     "options": [
         "Sender address exactly matches the official domain and the message references you specifically",
         "The email uses general greetings and a mismatched sender address",
         "The message demands immediate action with threats",
         "The email contains poor spelling and odd links"
     ],
     "correct": 0,
     "explain": "A correct sender domain and contextual personalization are indicators but still verify via official channels."},

    {"question": "What is a safe response to a suspicious credential request?",
     "options": [
         "Ignore and verify with the service using their official website or support number",
         "Provide your password to quickly resolve the issue",
         "Click links and enter credentials to test it",
         "Share it with coworkers"
     ],
     "correct": 0,
     "explain": "Never share credentials; verify independently through official websites or phone support."},

    {"question": "If a link text says 'bank.example.com' but the hovered URL points to 'malicious.example', this is:",
     "options": [
         "Likely a spoofed link and potentially malicious",
         "Definitely safe",
         "A sign of high reputation",
         "A system update"
     ],
     "correct": 0,
     "explain": "Link text can be forged; always inspect the actual URL before visiting."},

    {"question": "Phishing attachments often contain what risk?",
     "options": [
         "Malicious macros or executables that run code",
         "Only harmless images",
         "Faster system performance",
         "Automatic backups"
     ],
     "correct": 0,
     "explain": "Attachments may include malware or scripts; only open trusted files and scan them first."},

    {"question": "A common phishing trick to steal login info is to:",
     "options": [
         "Redirect you to a look-alike login page that captures credentials",
         "Send a friendly meme",
         "Offer faster download speeds",
         "Hide in system updates"
     ],
     "correct": 0,
     "explain": "Attackers host spoofed pages that mimic real sites to capture username and password."},

    {"question": "Which action helps reduce phishing risk for your accounts?",
     "options": [
         "Enabling two-factor authentication (2FA)",
         "Using same password everywhere",
         "Posting credentials publicly",
         "Disabling email filters"
     ],
     "correct": 0,
     "explain": "2FA adds a second verification factor, reducing the effectiveness of stolen credentials."},

    {"question": "If you suspect a message is phishing, you should:",
     "options": [
         "Report it to your organization's security or email provider",
         "Ignore and delete always",
         "Reply to ask for more details",
         "Click all links to investigate"
     ],
     "correct": 0,
     "explain": "Reporting helps security teams block the threat and warn others."},

    {"question": "Business Email Compromise (BEC) typically targets:",
     "options": [
         "Employees with privilege to transfer funds or access sensitive info",
         "Only external customers",
         "Only social media accounts",
         "Video streaming services"
     ],
     "correct": 0,
     "explain": "BEC attacks impersonate executives or vendors to trick privileged employees into transferring money or data."},

    {"question": "What is spear phishing?",
     "options": [
         "A targeted phishing attack against a specific person or group",
         "A random spam campaign",
         "A tool for encrypting email",
         "A harmless newsletter"
     ],
     "correct": 0,
     "explain": "Spear phishing uses personalized information to increase credibility and success rate."},

    {"question": "SMS-based phishing (smishing) often tries to:",
     "options": [
         "Get you to click links or call numbers that impersonate services",
         "Deliver system updates",
         "Send harmless jokes",
         "Improve battery life"
     ],
     "correct": 0,
     "explain": "Smishing uses text messages to trick victims into visiting malicious sites or calling scam numbers."},

    {"question": "Voice phishing (vishing) leverages:",
     "options": [
         "Phone calls that impersonate trusted organizations to extract info",
         "Only email attachments",
         "Technical encryption",
         "Video content"
     ],
     "correct": 0,
     "explain": "Vishing relies on social engineering over voice calls to obtain credentials or approvals."},

    {"question": "A red flag in recovery emails is:",
     "options": [
         "Unexpected password reset emails you did not request",
         "A scheduled system backup notice you requested",
         "An internal team announcement you subscribed to",
         "A notification from your calendar"
     ],
     "correct": 0,
     "explain": "Unsolicited password reset messages can indicate attempted account takeover; verify immediately."},

    {"question": "What is 'URL punycode' abuse used for in attacks?",
     "options": [
         "To create domain names that visually resemble real domains",
         "To speed up websites",
         "To backup files",
         "To encrypt email"
     ],
     "correct": 0,
     "explain": "Punycode can create visually similar domains using international characters to spoof legitimate sites."},

    {"question": "When evaluating an email, a mismatched 'From' display name and email address is:",
     "options": [
         "A sign to verify further because it may be spoofed",
         "Always safe",
         "Required for newsletters",
         "A firewall setting"
     ],
     "correct": 0,
     "explain": "Display names are easy to forge; check the actual email address domain for legitimacy."},

    {"question": "Attackers sometimes use shortened URLs to:",
     "options": [
         "Obscure destination and hide malicious links",
         "Speed up downloads",
         "Encrypt traffic",
         "Improve SEO"
     ],
     "correct": 0,
     "explain": "Short URLs hide the true destination; preview them through safe services before opening."},

    {"question": "Which habit reduces phishing success at scale?",
     "options": [
         "Security awareness training and simulated phishing exercises",
         "Sharing passwords for convenience",
         "Disabling email scanning",
         "Using the same password everywhere"
     ],
     "correct": 0,
     "explain": "Education and simulation improve recognition and reduce user-mediated compromises."},

    {"question": "A legitimate service will rarely ask for your password via:",
     "options": [
         "Email or instant message",
         "Secure website login directly",
         "Official in-app prompts",
         "Company support portal"
     ],
     "correct": 0,
     "explain": "Services do not request passwords through email; use official login pages instead."},

    {"question": "A common bait in phishing is an 'invoice' or 'payment' request that:",
     "options": [
         "Pressures a quick transfer or click to view details",
         "Explains long policy documents",
         "Requests public praise",
         "Invites to a free event only"
     ],
     "correct": 0,
     "explain": "Financial urgency is a strong lure because recipients may act without verification."},

    {"question": "If you receive an email claiming your account is locked and provides a link to 'unlock', you should:",
     "options": [
         "Go to the official website manually without using the link",
         "Click the link and enter credentials right away",
         "Reply with your password",
         "Forward to friends"
     ],
     "correct": 0,
     "explain": "Navigate directly to the official site to check the account instead of following email links."},

    {"question": "Phishing kits are:",
     "options": [
         "Prebuilt tools attackers use to create fake login pages quickly",
         "Security patches",
         "Email marketing templates from reputable companies",
         "Legitimate backup utilities"
     ],
     "correct": 0,
     "explain": "Kits allow attackers to deploy convincing spoofed sites with little effort."},

    {"question": "Using an email provider with strong spam filtering helps because:",
     "options": [
         "It reduces the number of phishing emails reaching the inbox",
         "It guarantees 100% protection",
         "It eliminates need for passwords",
         "It speeds up the computer"
     ],
     "correct": 0,
     "explain": "Filtering reduces exposure to malicious messages, though users should stay vigilant."},

    {"question": "A 'displayed' link that contains an IP address rather than a domain can be suspicious because:",
     "options": [
         "Many legitimate sites use domains, not raw IPs, and attackers may host malicious pages on IP addresses",
         "IP addresses are always safe",
         "IP addresses speed up downloads",
         "IP addresses encrypt your data"
     ],
     "correct": 0,
     "explain": "Legitimate services typically use domain names; IP-based links can be a sign of malicious hosting."},

    {"question": "When an email asks for sensitive personal information (like SSN) via message, the safe action is to:",
     "options": [
         "Do not provide it and verify the request through trusted official channels",
         "Provide it immediately",
         "Post it publicly for verification",
         "Ignore every official request always"
     ],
     "correct": 0,
     "explain": "Never share sensitive data via unverified messages; confirm via official contact methods."},

    {"question": "A social engineering email that references a recent event about you likely means:",
     "options": [
         "The attacker researched you and tailored the message (spear phishing)",
         "The message is harmless",
         "It is a system update",
         "It came from a trusted vendor"
     ],
     "correct": 0,
     "explain": "Personalized details increase phishing credibility; treat such messages with caution."}
]

# ------------------------------------------------------------
# CATEGORY: Password Security (30)
# ------------------------------------------------------------
passwords = [
    {"question": "Which approach most improves password strength?",
     "options": [
         "Long, unique passphrases using several words or characters",
         "Short passwords with special characters",
         "Using the same password everywhere",
         "Writing passwords on sticky notes"
     ],
     "correct": 0,
     "explain": "Length and uniqueness increase entropy; passphrases are easier to remember and harder to brute force."},

    {"question": "Why is using a password manager recommended?",
     "options": [
         "It safely stores and generates unique passwords for each account",
         "It shares passwords with coworkers",
         "It eliminates the need for passwords entirely",
         "It posts them publicly"
     ],
     "correct": 0,
     "explain": "Managers enable unique strong credentials without memorization and improve security hygiene."},

    {"question": "What is the best practice when creating passwords for important accounts?",
     "options": [
         "Make them long, unique, and avoid predictable phrases",
         "Use your birthdate for convenience",
         "Use 'password' with an exclamation mark",
         "Use the same password for multiple services"
     ],
     "correct": 0,
     "explain": "Long, unpredictable passwords resist guessing and prevent credential reuse risks."},

    {"question": "Why avoid password reuse across services?",
     "options": [
         "A breach at one site can compromise other accounts using the same credential",
         "It saves time",
         "It reduces the need for updates",
         "It is recommended by security experts"
     ],
     "correct": 0,
     "explain": "Reused passwords create a single point of failure that attackers exploit in credential stuffing attacks."},

    {"question": "Which is a secure option for account recovery instead of public data?",
     "options": [
         "Use an email or phone you control and keep recovery methods private",
         "Use answers that are easily guessable on social media",
         "Post recovery keys publicly",
         "Share your recovery with coworkers"
     ],
     "correct": 0,
     "explain": "Keep recovery channels private and secure to prevent account takeovers via weak recovery data."},

    {"question": "What does 'entropy' mean regarding passwords?",
     "options": [
         "A measure of unpredictability and resistance to guessing",
         "How fast the password types",
         "How shiny it looks",
         "How many people know it"
     ],
     "correct": 0,
     "explain": "Entropy quantifies how hard a password is to guess; higher entropy is better."},

    {"question": "Why are passphrases often recommended over short complex passwords?",
     "options": [
         "They can be longer and easier to remember while providing strong entropy",
         "They are always shorter",
         "They never contain symbols",
         "They must be changed daily"
     ],
     "correct": 0,
     "explain": "Longer passphrases add complexity without forcing hard-to-remember character patterns."},

    {"question": "Which action improves protection even if a password is compromised?",
     "options": [
         "Enabling two-factor authentication (2FA)",
         "Publishing the password on social media",
         "Using a short PIN only",
         "Removing backups"
     ],
     "correct": 0,
     "explain": "2FA requires a second verifier (code or hardware) that helps prevent unauthorized access using stolen passwords."},

    {"question": "When should you change your password?",
     "options": [
         "If you suspect compromise or the service notifies of a breach",
         "Only when the site forces you yearly",
         "Never",
         "Every hour"
     ],
     "correct": 0,
     "explain": "Change upon suspected exposure; arbitrary frequent forced changes can cause weak choices."},

    {"question": "What is credential stuffing?",
     "options": [
         "Automated reuse of breached username/password pairs across many sites",
         "A backup process",
         "A tool to compress files",
         "A method to encrypt passwords"
     ],
     "correct": 0,
     "explain": "Attackers use known credentials across sites to gain access when users reuse passwords."},

    {"question": "Why should you allow password paste when using managers?",
     "options": [
         "It enables managers to input complex passwords easily and avoid typing errors",
         "It always creates unsafe conditions",
         "It posts passwords to public logs",
         "It is required by all browsers"
     ],
     "correct": 0,
     "explain": "Allowing paste supports secure manager workflows and avoids users choosing weaker passwords for convenience."},

    {"question": "What is a hardware security key used for?",
     "options": [
         "A physical second factor (FIDO, U2F) for strong authentication",
         "To store music files",
         "To speed up the network",
         "To replace the antivirus"
     ],
     "correct": 0,
     "explain": "Hardware keys provide strong phishing-resistant second-factor authentication."},

    {"question": "Why are easily guessable patterns bad (e.g., 'abcd1234')?",
     "options": [
         "They are low entropy and vulnerable to dictionary and brute-force attacks",
         "They speed up login",
         "They are always required",
         "They protect data"
     ],
     "correct": 0,
     "explain": "Predictable patterns are easy for attackers to guess or include in attack lists."},

    {"question": "Which is safest for sharing credentials with a colleague briefly?",
     "options": [
         "Use a dedicated secure team password manager sharing feature",
         "Send it via plain email",
         "Write it on a sticky note",
         "Announce publicly"
     ],
     "correct": 0,
     "explain": "Use secure sharing controls that log access and encrypt stored credentials."},

    {"question": "What is multi-factor authentication (MFA)?",
     "options": [
         "Use of two or more categories of authentication: something you know, have, or are",
         "Using two passwords only",
         "Using a single long password",
         "Sharing passwords"
     ],
     "correct": 0,
     "explain": "MFA combines independent factors to strengthen authentication beyond a password alone."},

    {"question": "Why avoid hints and security questions based on public data?",
     "options": [
         "Answers may be discoverable online and allow account recovery abuse",
         "They always block attackers",
         "They speed up authentication",
         "They encrypt the account"
     ],
     "correct": 0,
     "explain": "Publicly available answers can be exploited to reset or take over accounts."},

    {"question": "What is a 'password spray' attack?",
     "options": [
         "Trying a few common passwords across many accounts to avoid lockouts",
         "Spraying water on a keyboard",
         "Encrypting passwords automatically",
         "A form of spam"
     ],
     "correct": 0,
     "explain": "Spraying uses low-volume attempts across accounts to evade detection and account lockout thresholds."},

    {"question": "Secure password storage by services should use:",
     "options": [
         "Salted, slow hashing (e.g., bcrypt, Argon2) rather than plaintext or weak hashes",
         "Plaintext storage",
         "Reversible encryption without protections",
         "Storing on public pages"
     ],
     "correct": 0,
     "explain": "Salting and slow hashing mitigate offline cracking if databases are leaked."},

    {"question": "When using a shared or public computer, you should:",
     "options": [
         "Avoid entering sensitive credentials and log out and clear browsers if needed",
         "Save passwords in the browser",
         "Leave sessions open",
         "Install unknown software"
     ],
     "correct": 0,
     "explain": "Public machines may be compromised; use trusted devices or private browsing and log out fully."},

    {"question": "What is the benefit of passphrase complexity over short complex passwords?",
     "options": [
         "Long passphrases provide higher entropy even if predictable words are used",
         "They always break security",
         "They replace 2FA",
         "They shorten login times"
     ],
     "correct": 0,
     "explain": "Length combined with randomness increases difficulty for attackers to guess or brute force."},

    {"question": "What should you do if a service you use notifies a credential breach?",
     "options": [
         "Change passwords for that service and any other services using the same credentials",
         "Do nothing",
         "Share your credentials publicly",
         "Wait for months before acting"
     ],
     "correct": 0,
     "explain": "Promptly changing affected credentials reduces the risk of account takeover."},

    {"question": "What is 'phishing-resistant' authentication?",
     "options": [
         "Authentication methods (like hardware tokens) that prevent attackers from capturing credentials on fake sites",
         "Simple passwords",
         "Text file backups",
         "Posting credentials in forums"
     ],
     "correct": 0,
     "explain": "Methods that bind to the legitimate site or use asymmetric keys protect against credential harvesting."},

    {"question": "Why is it risky to store passwords in plain text on cloud notes?",
     "options": [
         "They can be accessed if the account is compromised and often lack encryption at rest by default",
         "It improves security",
         "It speeds synchronization",
         "Providers always protect them automatically"
     ],
     "correct": 0,
     "explain": "Plain text storage exposes credentials to compromise; use encrypted password managers instead."},

    {"question": "What is 'credential rotation' for service accounts?",
     "options": [
         "Regularly updating service account credentials to reduce exposure risk",
         "Stopping services",
         "Sharing credentials with humans",
         "Never changing them"
     ],
     "correct": 0,
     "explain": "Rotation reduces the window of opportunity if credentials are leaked."},

    {"question": "Why avoid using predictable sequences (e.g., '123456')?",
     "options": [
         "They are the first guesses attackers try and are extremely weak",
         "They speed up login",
         "They are required by security",
         "They reduce memory"
     ],
     "correct": 0,
     "explain": "Common sequences are trivial for attackers and widely present in breach lists."},

    {"question": "What is a recommended minimum password length for good security practice?",
     "options": [
         "At least 12 characters for user accounts (longer is better)",
         "2 characters",
         "4 digits only",
         "1 character"
     ],
     "correct": 0,
     "explain": "Longer length increases combinations and resistance to brute-force attacks."}
]

# ------------------------------------------------------------
# CATEGORY: Access Control (30)
# ------------------------------------------------------------
access_control = [
    {"question": "What is the principle of least privilege?",
     "options": [
         "Granting users only the access they need to perform their tasks",
         "Making everyone an administrator",
         "Sharing admin passwords freely",
         "Never changing permissions"
     ],
     "correct": 0,
     "explain": "Minimizing permissions reduces potential damage if an account is compromised."},

    {"question": "What is role-based access control (RBAC)?",
     "options": [
         "Assigning permissions to roles and assigning users to those roles",
         "Giving each user full admin rights",
         "Sharing passwords among all staff",
         "Using no access rules"
     ],
     "correct": 0,
     "explain": "RBAC simplifies management by grouping permissions into roles aligned with job functions."},

    {"question": "Why keep access logs?",
     "options": [
         "To audit and detect unauthorized access and support incident investigations",
         "To slow down the system intentionally",
         "To store passwords",
         "To replace backups"
     ],
     "correct": 0,
     "explain": "Logs are critical for detecting suspicious activity and reconstructing incidents."},

    {"question": "What is separation of duties?",
     "options": [
         "Distributing tasks so no single user has control over all steps in sensitive processes",
         "Giving one person all responsibilities",
         "Combining unrelated permissions in one role",
         "Removing all controls"
     ],
     "correct": 0,
     "explain": "Separation reduces risk of fraud and accidental misuse by requiring multiple actors for critical tasks."},

    {"question": "What does 'account provisioning' refer to?",
     "options": [
         "Creating and configuring user accounts with appropriate permissions when needed",
         "Deleting system files",
         "Encryption of all emails",
         "Sharing passwords publicly"
     ],
     "correct": 0,
     "explain": "Provisioning ensures users get correct access and that access is revoked when no longer needed."},

    {"question": "What is an access control list (ACL)?",
     "options": [
         "A list that specifies which users or system processes can access resources",
         "A music playlist",
         "A backup schedule",
         "A firewall patch"
     ],
     "correct": 0,
     "explain": "ACLs define who can read, write, or execute resources under specific conditions."},

    {"question": "Why implement strong password policies for privileged accounts?",
     "options": [
         "Because privileged accounts are high-value targets and require stronger controls",
         "Because they slow down the system",
         "To enforce same password everywhere",
         "To hide accounts from admins"
     ],
     "correct": 0,
     "explain": "Privileged accounts have greater access; stronger credentials and MFA protect them from takeover."},

    {"question": "What does 'just-in-time' access provide?",
     "options": [
         "Temporary elevated permissions only for the time needed to complete a task",
         "Permanent admin rights",
         "Public access to resources",
         "Open firewall rules"
     ],
     "correct": 0,
     "explain": "Just-in-time reduces standing privileges and limits exposure windows."},

    {"question": "Why remove access promptly when an employee leaves?",
     "options": [
         "To prevent former users from accessing systems and sensitive data",
         "To save disk space",
         "To speed up their email",
         "To keep backups"
     ],
     "correct": 0,
     "explain": "Timely deprovisioning prevents unauthorized access by ex-employees or freelancers."},

    {"question": "What is multifactor access control?",
     "options": [
         "Requiring more than one type of authentication factor to grant access",
         "Using just passwords always",
         "Granting anonymous access",
         "Using insecure tokens"
     ],
     "correct": 0,
     "explain": "MFA strengthens access control by requiring independent proofs of identity."},

    {"question": "What is attribute-based access control (ABAC)?",
     "options": [
         "Access decisions based on attributes of users, resources, and context",
         "Assigning everyone the same rights",
         "Sharing files publicly",
         "Using only IP-based rules"
     ],
     "correct": 0,
     "explain": "ABAC uses flexible policies considering user and resource attributes and context for fine-grained control."},

    {"question": "What is a service account?",
     "options": [
         "An account used by applications or services rather than human users",
         "A personal social media account",
         "A public guest account",
         "A music streaming account"
     ],
     "correct": 0,
     "explain": "Service accounts require special handling, least privilege, and credential rotation."},

    {"question": "Why rotate credentials for high-privilege accounts?",
     "options": [
         "To limit exposure if credentials are leaked or compromised",
         "To slow down the system",
         "To share them more widely",
         "Because frequency is irrelevant"
     ],
     "correct": 0,
     "explain": "Rotation reduces the time window an attacker can use stolen credentials."},

    {"question": "What is access certification (attestation)?",
     "options": [
         "Periodic review of who has access to ensure only authorized users retain permissions",
         "Daily password changes",
         "Disabling logs",
         "Public posting of credentials"
     ],
     "correct": 0,
     "explain": "Attestation ensures permissions remain appropriate and helps detect privilege creep."},

    {"question": "Why is multi-account separation (least privilege by account type) useful?",
     "options": [
         "To limit potential damage by separating duties and reducing unnecessary rights",
         "To merge roles into a single admin account",
         "To simplify sharing passwords",
         "To eliminate logs"
     ],
     "correct": 0,
     "explain": "Separate accounts for admin tasks reduce the risk of accidental misuse or compromise."},

    {"question": "What is the risk of shared generic accounts without tracking?",
     "options": [
         "Lack of accountability and difficulty auditing who did what",
         "Faster task completion",
         "Better security",
         "Automatic backups"
     ],
     "correct": 0,
     "explain": "Individual accounts with logging provide traceability; shared accounts obscure responsibility."},

    {"question": "What is 'privilege creep'?",
     "options": [
         "When users accumulate permissions over time they no longer need",
         "A malware type",
         "A network protocol",
         "A database backup"
     ],
     "correct": 0,
     "explain": "Privilege creep increases risk; periodic reviews and role management prevent it."},

    {"question": "Why limit admin console access to a small set of IPs or devices?",
     "options": [
         "To reduce exposure and make it harder for attackers to reach the management interfaces",
         "To speed up the internet",
         "To allow everyone to login",
         "To disable MFA"
     ],
     "correct": 0,
     "explain": "Access restrictions reduce attack surface for critical management functions."},

    {"question": "What is the main purpose of an identity provider (IdP)?",
     "options": [
         "Authenticate users centrally and provide identity assertions to applications",
         "Scan for malware only",
         "Replace all firewalls",
         "Store public posts"
     ],
     "correct": 0,
     "explain": "IdPs centralize authentication and federation for single sign-on and access control."},

    {"question": "Why enforce session timeouts for sensitive systems?",
     "options": [
         "To reduce the window for unattended sessions to be misused if left open",
         "To make sessions infinite",
         "To store passwords",
         "To publish logs publicly"
     ],
     "correct": 0,
     "explain": "Session timeouts protect against unauthorized access from forgotten or left-open sessions."},

    {"question": "What is the role of privileged access management (PAM)?",
     "options": [
         "Manage, monitor, and control privileged credentials and sessions",
         "Share admin passwords on sticky notes",
         "Disable logs",
         "Make everyone an admin"
     ],
     "correct": 0,
     "explain": "PAM tools control admin access, record sessions, and rotate credentials for high-value accounts."},

    {"question": "Why apply separation between production and development environments?",
     "options": [
         "To prevent accidental or malicious changes in production and limit exposure of real data",
         "To improve game speed",
         "To merge all codebases",
         "To skip backups"
     ],
     "correct": 0,
     "explain": "Isolation reduces risk and prevents nonproduction code or users from affecting live systems."},

    {"question": "What is just-in-case administrative access?",
     "options": [
         "Permanent, unused admin rights kept for emergencies (not recommended without controls)",
         "Temporary permissions with auditing",
         "A password manager",
         "A firewall rule"
     ],
     "correct": 0,
     "explain": "Standing emergency access should be controlled and monitored; temporary elevation is safer."},

    {"question": "What is an entitlement review?",
     "options": [
         "A review of users' permissions to ensure they are still appropriate",
         "A software update",
         "A backup process",
         "Deleting user accounts automatically"
     ],
     "correct": 0,
     "explain": "Entitlement reviews detect over-privileged accounts and correct permission drift."}
]

# ------------------------------------------------------------
# CATEGORY: Malware (30)
# ------------------------------------------------------------
malware = [
    {"question": "What is malware?",
     "options": [
         "Software designed to damage, steal, or exploit systems",
         "A type of backup",
         "A harmless application",
         "A social media trend"
     ],
     "correct": 0,
     "explain": "Malware includes viruses, worms, trojans, ransomware, and spyware used to harm systems or users."},

    {"question": "Ransomware primarily does what?",
     "options": [
         "Encrypts files and demands payment for decryption",
         "Speeds up computers",
         "Deletes internet history",
         "Improves battery life"
     ],
     "correct": 0,
     "explain": "Ransomware denies access to data until a ransom is paid or backups are used to recover."},

    {"question": "Why keep software and OS updated?",
     "options": [
         "Updates patch security vulnerabilities attackers exploit",
         "They only change fonts",
         "They always cause infections",
         "They stop all hackers forever"
     ],
     "correct": 0,
     "explain": "Timely updates reduce the window attackers have to exploit known vulnerabilities."},

    {"question": "Which is a common infection vector for malware?",
     "options": [
         "Malicious email attachments or downloads from untrusted sites",
         "Official system updates only",
         "Reading articles",
         "Using a password manager"
     ],
     "correct": 0,
     "explain": "Untrusted files can contain payloads that execute malicious code when opened."},

    {"question": "What is 'drive-by' download?",
     "options": [
         "Malware that installs when you visit a compromised website without explicit download",
         "A legitimate software update",
         "A file-sharing service",
         "A website speed optimization"
     ],
     "correct": 0,
     "explain": "Compromised sites can exploit browser vulnerabilities to install malware silently."},

    {"question": "What should you do if you suspect malware on your machine?",
     "options": [
         "Disconnect from networks, run a trusted scanner, and follow incident response steps",
         "Keep using it normally",
         "Share it with friends",
         "Delete system files randomly"
     ],
     "correct": 0,
     "explain": "Isolate the device and scan with reliable tools; follow containment and recovery procedures."},

    {"question": "What is a trojan?",
     "options": [
         "Malicious software disguised as legitimate software",
         "A firewall configuration",
         "An email protocol",
         "A backup routine"
     ],
     "correct": 0,
     "explain": "Trojans trick users into installing them to perform malicious actions."},

    {"question": "What is a worm?",
     "options": [
         "Self-replicating malware that spreads across networks without user action",
         "A type of antivirus",
         "A browser extension",
         "A password manager"
     ],
     "correct": 0,
     "explain": "Worms propagate autonomously and can rapidly infect many systems."},

    {"question": "How do antivirus and endpoint protection help?",
     "options": [
         "Detect and block known threats and suspicious behavior as part of layered defenses",
         "Guarantee perfect security",
         "Backup all files automatically",
         "Replace firewalls entirely"
     ],
     "correct": 0,
     "explain": "They are an important layer but should be combined with updates, backups, and user awareness."},

    {"question": "What is 'fileless' malware?",
     "options": [
         "Malware that lives in memory or uses legitimate tools rather than dropping files to disk",
         "A harmless process",
         "A software installer",
         "A browser plugin"
     ],
     "correct": 0,
     "explain": "Fileless attacks use memory or trusted system tools to evade detection by file-based scanners."},

    {"question": "Why maintain offline or immutable backups?",
     "options": [
         "To recover from ransomware or destructive malware even if live systems are encrypted",
         "To speed up the network",
         "To share sensitive data easily",
         "To expose backups publicly"
     ],
     "correct": 0,
     "explain": "Offline backups prevent ransomware from encrypting all copies of your data."},

    {"question": "What is spyware?",
     "options": [
         "Malware that collects information about users without consent",
         "A system cleaning tool",
         "A firewall rule",
         "A password manager"
     ],
     "correct": 0,
     "explain": "Spyware captures keystrokes, screenshots, or other private data to exfiltrate it to attackers."},

    {"question": "Which practice helps limit malware spread in a network?",
     "options": [
         "Network segmentation and principle of least privilege",
         "Removing all passwords",
         "Turning off logs",
         "Allowing all inbound traffic"
     ],
     "correct": 0,
     "explain": "Segmentation contains outbreaks and reduces lateral movement opportunities."},

    {"question": "Why verify software sources before installing?",
     "options": [
         "To avoid installing tampered or malicious installers from untrusted sources",
         "To always get the fastest version",
         "To improve screen brightness",
         "To share installers freely"
     ],
     "correct": 0,
     "explain": "Official vendor sources reduce the chance of installing maliciously modified software."},

    {"question": "What is malicious macro-enabled document risk?",
     "options": [
         "Documents that run macros can execute code and deliver malware if macros are enabled",
         "They are always safe",
         "They speed up document load",
         "They backup files"
     ],
     "correct": 0,
     "explain": "Disable macros by default and only enable them for trusted sources."},

    {"question": "Why use application allowlists?",
     "options": [
         "To allow only approved programs to run and block unknown executables",
         "To allow everything by default",
         "To remove security updates",
         "To share programs widely"
     ],
     "correct": 0,
     "explain": "Allowlisting prevents unapproved software and reduces risk of malware execution."},

    {"question": "What is a callback in malware behavior?",
     "options": [
         "When malware contacts a command-and-control server to receive instructions",
         "A customer service call",
         "A system update check",
         "A backup confirmation"
     ],
     "correct": 0,
     "explain": "Callbacks enable remote control and data exfiltration."},

    {"question": "What role does user privilege play in malware impact?",
     "options": [
         "Higher privileges allow malware to cause greater damage or persistence",
         "Privileges have no effect",
         "Lower privileges increase malware power",
         "Privileges make backups faster"
     ],
     "correct": 0,
     "explain": "Limiting user privileges reduces what malware can alter or access."},

    {"question": "Why scan downloads before opening?",
     "options": [
         "To detect known malware signatures or suspicious traits before execution",
         "To speed up the download",
         "To publish them on social media",
         "To increase system temperature"
     ],
     "correct": 0,
     "explain": "Scanning helps identify threats before they run on your system."},

    {"question": "How can attackers achieve persistence on a system?",
     "options": [
         "By modifying startup entries, services, or scheduled tasks to survive reboots",
         "By uninstalling programs",
         "By updating the antivirus",
         "By defragmenting the disk"
     ],
     "correct": 0,
     "explain": "Persistence mechanisms allow malware to remain across reboots and regain control."},

    {"question": "What is a 'dropper' in malware terminology?",
     "options": [
         "A program that installs additional malware payloads on a victim system",
         "A backup manager",
         "A firewall rule",
         "An email client"
     ],
     "correct": 0,
     "explain": "Droppers deliver and install more harmful components after initial compromise."},

    {"question": "Why keep least-privilege on services and containers?",
     "options": [
         "To minimize the potential damage if those processes are exploited",
         "To increase complexity only",
         "To remove logs",
         "To speed builds"
     ],
     "correct": 0,
     "explain": "Limiting runtime privileges reduces the blast radius of an exploited service."},

    {"question": "What is sandboxing used for?",
     "options": [
         "Running untrusted code in isolated environments to limit harm and analyze behavior",
         "To make code run faster in production",
         "To replace backups",
         "To remove security updates"
     ],
     "correct": 0,
     "explain": "Sandboxes contain untrusted actions and prevent system-wide damage."},

    {"question": "Why avoid pirated software?",
     "options": [
         "It often bundles malware and lacks vendor support and updates",
         "It is always safe",
         "It improves security",
         "It comes with warranties"
     ],
     "correct": 0,
     "explain": "Pirated installers are a common vector for bundled malware and provide no security updates."},

    {"question": "What is the 'kill chain' concept used for?",
     "options": [
         "Modeling attack stages from reconnaissance to exfiltration to inform defenses",
         "A tool to backup files",
         "A firewall configuration file",
         "A random network protocol"
     ],
     "correct": 0,
     "explain": "Understanding stages helps defenders detect and interrupt attacks at multiple points."}
]

# ------------------------------------------------------------
# CATEGORY: Social Engineering (30)
# ------------------------------------------------------------
social_engineering = [
    {"question": "What is social engineering?",
     "options": [
         "Manipulating people to reveal information or perform actions that compromise security",
         "A malware scanner",
         "A firewall update",
         "A backup schedule"
     ],
     "correct": 0,
     "explain": "Social engineering exploits human trust and psychology rather than technical vulnerabilities."},

    {"question": "What is pretexting?",
     "options": [
         "Inventing a plausible story to trick targets into divulging information",
         "Formatting documents",
         "Encrypting files",
         "Installing updates"
     ],
     "correct": 0,
     "explain": "Pretexting builds trust through a fabricated identity or scenario to extract data."},

    {"question": "How does tailgating work?",
     "options": [
         "An attacker follows an authorized person into a secure area without credentials",
         "A network protocol",
         "A harmless friendly greeting",
         "A type of antivirus"
     ],
     "correct": 0,
     "explain": "Physical access attacks exploit human courtesy to bypass entry controls."},

    {"question": "Why limit personal details on social media?",
     "options": [
         "Attackers use details to craft believable social engineering attacks or guess security answers",
         "It makes profiles less interesting",
         "It speeds up browsers",
         "It is required by law"
     ],
     "correct": 0,
     "explain": "Public personal info makes it easier for attackers to impersonate or answer recovery questions."},

    {"question": "What is baiting?",
     "options": [
         "Offering something enticing (like free downloads) to get users to perform risky actions",
         "A system cleaning task",
         "A firewall tuning",
         "A backup policy"
     ],
     "correct": 0,
     "explain": "Baiting lures victims with attractive offers that often deliver malware or request credentials."},

    {"question": "How can verification through a second channel reduce social engineering?",
     "options": [
         "Independent confirmation (like a phone call to a known number) verifies identity beyond a single contact method",
         "It always removes the need for passwords",
         "It duplicates credentials publicly",
         "It disables logging"
     ],
     "correct": 0,
     "explain": "Using separate channels prevents attackers who control only one channel from impersonating contacts."},

    {"question": "Why should employees be cautious about unexpected requests for wire transfers?",
     "options": [
         "They could be fraudulent instructions from attackers impersonating executives",
         "They are always legitimate",
         "They speed up accounting",
         "They come from the bank always"
     ],
     "correct": 0,
     "explain": "Funds transfer frauds rely on impersonation and urgency; verify via known contact methods."},

    {"question": "What is quid pro quo social engineering?",
     "options": [
         "Offering a service or benefit in exchange for credentials or access",
         "A type of encryption",
         "A software patch",
         "A backup procedure"
     ],
     "correct": 0,
     "explain": "Attackers promise help or goods to manipulate targets into unsafe actions."},

    {"question": "How can companies reduce social engineering risk?",
     "options": [
         "Regular training, clear escalation procedures, and verification policies",
         "Sharing passwords openly",
         "Removing authentication",
         "Encouraging public posts"
     ],
     "correct": 0,
     "explain": "Training and enforced verification reduce success of social attacks."},

    {"question": "What is an 'insider threat' in social engineering context?",
     "options": [
         "A trusted person who intentionally or accidentally misuses access",
         "A network scanner",
         "A firewall device",
         "A backup system"
     ],
     "correct": 0,
     "explain": "Insiders can cause harm through malicious action or negligence; controls and monitoring help mitigate this."},

    {"question": "Why verify changes to payment details requested by email?",
     "options": [
         "Attackers may spoof vendors to redirect payments; verify via known vendor contacts",
         "To speed transfers",
         "To automate accounting",
         "To reduce logging"
     ],
     "correct": 0,
     "explain": "Verification prevents wire fraud and invoice manipulation schemes."},

    {"question": "In social engineering, 'authority' is used to:",
     "options": [
         "Pressure targets to comply by impersonating managers or officials",
         "Only improve documentation",
         "Encrypt transmissions",
         "Update software"
     ],
     "correct": 0,
     "explain": "Impersonating authority exploits obedience to gain compliance without verification."},

    {"question": "Why should staff be taught not to share credentials over phone or email?",
     "options": [
         "Because attackers can spoof communications and those channels are not secure for credential exchange",
         "Because it speeds up helpdesk",
         "Because it improves backups",
         "Because it is required by social media"
     ],
     "correct": 0,
     "explain": "Credentials should only be entered into official login prompts, not shared via messages."},

    {"question": "What is 'shoulder surfing'?",
     "options": [
         "Observing someone entering credentials or PINs in public to steal them",
         "A type of malware",
         "A firewall rule",
         "A backup technique"
     ],
     "correct": 0,
     "explain": "Physical observation can expose secrets; use privacy screens and cover inputs in public."},

    {"question": "Why is a verification code via authenticator app more resistant to social engineering than SMS?",
     "options": [
         "Authenticator apps are less vulnerable to SIM swap attacks and interception",
         "SMS never delivers codes",
         "Apps always publish codes publicly",
         "SMS is always secure"
     ],
     "correct": 0,
     "explain": "Authenticator apps avoid SIM-based interception and are generally more secure than SMS for 2FA."},

    {"question": "What is a safe policy for external visitors in an office?",
     "options": [
         "Escort visitors, log their presence, and restrict access to sensitive areas",
         "Let them roam freely",
         "Share admin passwords with them",
         "Allow them to use any devices"
     ],
     "correct": 0,
     "explain": "Controls reduce the risk of physical social engineering and unauthorized access."},

    {"question": "What is 'piggybacking' related to physical security?",
     "options": [
         "When an attacker enters a secure area by following an authorized person who holds the door open",
         "A network attack",
         "A backup process",
         "A firewall patch"
     ],
     "correct": 0,
     "explain": "Piggybacking exploits human courtesy to bypass access controls."},

    {"question": "Which is an example of a safe verification practice?",
     "options": [
         "Call the requesting party on an independently verified number before taking sensitive action",
         "Reply to the same email asking for details",
         "Click links to verify identity",
         "Share your credentials to confirm identity"
     ],
     "correct": 0,
     "explain": "Independent verification prevents attackers from using compromised channels to impersonate others."},

    {"question": "What is 'reconnaissance' in social engineering?",
     "options": [
         "Collecting publicly available information about a target to craft believable scams",
         "An encryption algorithm",
         "A firewall setting",
         "A backup schedule"
     ],
     "correct": 0,
     "explain": "Reconnaissance gathers details like job role, contacts, and recent events to tailor attacks."},

    {"question": "Why restrict public posting of employee emails?",
     "options": [
         "To reduce the amount of targetable information available to scammers",
         "To hide contact information always",
         "To speed up website loading",
         "To improve SEO"
     ],
     "correct": 0,
     "explain": "Less public exposure reduces the opportunities for targeted social engineering."},

    {"question": "What is the recommended response to unsolicited help offers from 'IT'?",
     "options": [
         "Verify identity through official internal support channels before granting remote access",
         "Grant access immediately to resolve quickly",
         "Share credentials when asked",
         "Install unknown software"
     ],
     "correct": 0,
     "explain": "Use known helpdesk procedures to confirm requests are legitimate before allowing remote control."},

    {"question": "Why limit information in voicemail greetings?",
     "options": [
         "Too much personal or role information can aid attackers conducting pretexting",
         "It always improves security if you include full details",
         "It speeds up phone calls",
         "It encrypts voicemail automatically"
     ],
     "correct": 0,
     "explain": "Minimal public details reduce the data attackers can use for impersonation."},

    {"question": "What is a social engineering 'watering hole' attack?",
     "options": [
         "Compromising a website visited by target groups to serve malicious content",
         "A legitimate security patch",
         "A phishing email only",
         "A data backup tool"
     ],
     "correct": 0,
     "explain": "Attackers infect commonly used sites to reach multiple targets without direct phishing."},

    {"question": "Why use least-privilege for human resources and finance systems?",
     "options": [
         "These systems contain sensitive personal and financial data; limiting access reduces exposure",
         "To speed payroll",
         "To share data publicly",
         "To remove backups"
     ],
     "correct": 0,
     "explain": "Restricting access to only necessary personnel limits insider risk and external attack impact."}
]

# ------------------------------------------------------------
# CATEGORY: Email Security (30)
# ------------------------------------------------------------
email_security = [
    {"question": "Why is enabling spam and phishing filters recommended?",
     "options": [
         "They reduce malicious messages that reach users' inboxes",
         "They always remove 100% of threats",
         "They prevent software updates",
         "They make email faster"
     ],
     "correct": 0,
     "explain": "Filters block many threats before user interaction, but users should remain cautious."},

    {"question": "What is email encryption used for?",
     "options": [
         "Protecting the content of messages so only intended recipients can read them",
         "Deleting spam automatically",
         "Making attachments smaller",
         "Improving battery life"
     ],
     "correct": 0,
     "explain": "Encryption ensures confidentiality of message content during transit and storage."},

    {"question": "Why avoid enabling macros in documents from unknown senders?",
     "options": [
         "Macros can execute code and deliver malware if enabled",
         "They speed up document use",
         "They are always helpful",
         "They improve visuals"
     ],
     "correct": 0,
     "explain": "Only enable macros from trusted authors to avoid executing malicious code."},

    {"question": "What does DKIM do for email?",
     "options": [
         "Provides a cryptographic signature to help verify the sender's domain hasn't been spoofed",
         "Always encrypts attachments",
         "Blocks all spam automatically",
         "Sends attachments"
     ],
     "correct": 0,
     "explain": "DKIM signatures allow recipient systems to check that email content was authorized by the sending domain."},

    {"question": "What is SPF used to prevent?",
     "options": [
         "Spoofed senders by specifying permitted sending IPs for a domain",
         "Malicious attachments only",
         "Faster email delivery",
         "Automatic backups"
     ],
     "correct": 0,
     "explain": "SPF helps receiving servers detect spoofed messages by checking the sending IP against allowed lists."},

    {"question": "What is DMARC's role in email security?",
     "options": [
         "It coordinates SPF/DKIM results and tells receivers how to handle suspicious mail",
         "It backs up emails",
         "It encrypts email content by default",
         "It deletes spam automatically"
     ],
     "correct": 0,
     "explain": "DMARC policies instruct receivers to quarantine or reject unauthenticated mail for a domain."},

    {"question": "Why preview links rather than clicking in emails?",
     "options": [
         "To verify the actual destination and avoid spoofed or malicious sites",
         "To make pages load faster",
         "To encrypt links",
         "To report spam automatically"
     ],
     "correct": 0,
     "explain": "Previewing helps detect mismatches between visible text and true URL targets."},

    {"question": "What is best when receiving an unexpected attachment from a colleague?",
     "options": [
         "Verify with the sender via another channel before opening",
         "Open it immediately",
         "Forward to all contacts",
         "Upload to public sites"
     ],
     "correct": 0,
     "explain": "Confirming legitimacy helps avoid malicious attachments from spoofed or compromised accounts."},

    {"question": "Why use unique addresses or aliases for online signups?",
     "options": [
         "To identify which services leak or sell your email and reduce spam exposure",
         "To speed logins",
         "To share credentials",
         "To remove filters"
     ],
     "correct": 0,
     "explain": "Aliases help manage and limit the impact of data leaks and tracking."},

    {"question": "What is end-to-end email encryption?",
     "options": [
         "Only the sender and recipient can read the message; intermediaries cannot",
         "A way to mark spam",
         "A backup technique",
         "A phishing detection method"
     ],
     "correct": 0,
     "explain": "End-to-end encryption protects content across transit and storage from intermediaries."},

    {"question": "Why configure retention and deletion policies for email?",
     "options": [
         "To limit the amount of sensitive data stored and reduce exposure risk",
         "To keep everything forever",
         "To publish emails publicly",
         "To disable encryption"
     ],
     "correct": 0,
     "explain": "Retention policies balance legal, operational, and security needs by limiting unnecessary data storage."},

    {"question": "What is the risk of using email for highly sensitive data?",
     "options": [
         "Email systems may be intercepted or misdelivered; use secure transfers or encrypted channels for sensitive material",
         "Email always prevents leaks",
         "Email is instantaneous and safe for secrets",
         "Email encrypts attachments automatically"
     ],
     "correct": 0,
     "explain": "Prefer secure file-sharing or encryption rather than plain email for sensitive information."},

    {"question": "What is an email header useful for?",
     "options": [
         "Investigating origin, path, and authentication details of a message",
         "Only for formatting fonts",
         "To speed downloads",
         "To encrypt messages"
     ],
     "correct": 0,
     "explain": "Headers contain routing and authentication metadata valuable in identifying spoofing or source."},

    {"question": "Why avoid sending credentials over email?",
     "options": [
         "Email can be intercepted or forwarded; credentials should be entered only on verified sites",
         "Email automatically secures credentials",
         "Email deletes them",
         "Email verifies them for you"
     ],
     "correct": 0,
     "explain": "Credentials in email increase exposure and risk of compromise."},

    {"question": "Why use email auto-forwarding rules carefully?",
     "options": [
         "Forward rules can accidentally expose sensitive mail if misconfigured or abused by attackers",
         "They always improve security",
         "They reduce spam automatically",
         "They disable encryption"
     ],
     "correct": 0,
     "explain": "Monitor outbound forwarding to prevent data leaks caused by rules set by users or attackers."},

    {"question": "Which is a best practice for email attachments?",
     "options": [
         "Use password-protected archives and share the password through a separate channel when necessary",
         "Always send plaintext passwords in attachments",
         "Attach executables to all emails",
         "Never scan attachments"
     ],
     "correct": 0,
     "explain": "Protected archives and separate password channels reduce risk of interception revealing content."},

    {"question": "Why enable multi-factor authentication for email accounts?",
     "options": [
         "Because email is a high-value target for account takeover and MFA reduces risk",
         "Because it slows down login unnecessarily",
         "Because it publishes email content",
         "Because it removes spam"
     ],
     "correct": 0,
     "explain": "Protecting email with MFA prevents attackers from using stolen passwords alone to gain access."},

    {"question": "What is 'mailbox compromise' impact?",
     "options": [
         "Attackers can intercept sensitive messages, reset other accounts, and impersonate the victim",
         "It only affects spam folders",
         "It always speeds up delivery",
         "It improves backups"
     ],
     "correct": 0,
     "explain": "Compromised mailboxes enable broad account takeover and fraud."},

    {"question": "Why use domain-based authentication standards (SPF/DKIM/DMARC)?",
     "options": [
         "To reduce spoofing and allow receivers to identify unauthenticated or malicious mail",
         "To make mail heavier",
         "To remove the need for TLS",
         "To increase open rates"
     ],
     "correct": 0,
     "explain": "Together these standards help receivers validate sender authenticity and handle suspicious mail."},

    {"question": "What is the best way to dispose of old email containing secrets?",
     "options": [
         "Permanently delete and ensure backups are cleaned according to policy",
         "Leave them forever",
         "Post them online",
         "Archive publicly"
     ],
     "correct": 0,
     "explain": "Secure disposal minimizes exposure of sensitive information over time."},

    {"question": "What is the advantage of using enterprise email gateways?",
     "options": [
         "They provide centralized filtering, DLP, and policies to reduce threats and leaks",
         "They replace passwords",
         "They eliminate need for training",
         "They automatically fix all vulnerabilities"
     ],
     "correct": 0,
     "explain": "Gateways enforce organization-level protections and content controls."},

    {"question": "Why be cautious with 'auto-complete' when addressing email?",
     "options": [
         "You may accidentally select the wrong contact and send sensitive info to unintended recipients",
         "Auto-complete is always secure",
         "It anonymizes recipients",
         "It encrypts attachments"
     ],
     "correct": 0,
     "explain": "Verify recipients before sending to avoid data leakage due to selection mistakes."},

    {"question": "What role does TLS play in email transport?",
     "options": [
         "Encrypts the SMTP session between mail servers to protect messages in transit",
         "Deletes spam automatically",
         "Compresses attachments to save space",
         "Authenticates user passwords"
     ],
     "correct": 0,
     "explain": "TLS protects mail in transit against eavesdropping between servers and clients."}
]

# ------------------------------------------------------------
# CATEGORY: Internet Safety & Network (30)
# ------------------------------------------------------------
internet_safety = [
    {"question": "Why is public Wi-Fi risky for sensitive activities?",
     "options": [
         "Traffic can be intercepted by others on the same network without encryption",
         "It always blocks websites",
         "It encrypts all traffic by default",
         "It speeds up banking"
     ],
     "correct": 0,
     "explain": "Untrusted networks may allow attackers to sniff unencrypted traffic and harvest credentials."},

    {"question": "What does HTTPS protect?",
     "options": [
         "Encryption and integrity of data between your browser and the web server",
         "The speed of a website always",
         "The number of ads shown",
         "Local file backups"
     ],
     "correct": 0,
     "explain": "HTTPS uses TLS to secure communications, preventing eavesdropping and tampering."},

    {"question": "What is the purpose of a VPN on public networks?",
     "options": [
         "Provide an encrypted tunnel to protect traffic from local network eavesdroppers",
         "Replace antivirus software",
         "Always speed up streaming",
         "Make Wi-Fi unnecessary"
     ],
     "correct": 0,
     "explain": "VPNs protect data on untrusted networks by encrypting traffic to a trusted endpoint."},

    {"question": "Which is an indicator of a secure website when logging in?",
     "options": [
         "A valid HTTPS certificate and correct domain",
         "Only colorful graphics",
         "A popup asking for your password immediately",
         "A random IP address in the address bar"
     ],
     "correct": 0,
     "explain": "Certificates and domains confirm you are connecting to the intended site over encrypted channel."},

    {"question": "What is DNS spoofing?",
     "options": [
         "An attack that returns false DNS responses to redirect users to malicious sites",
         "A backup routine",
         "An encryption algorithm",
         "A firewall update"
     ],
     "correct": 0,
     "explain": "Spoofed DNS can misdirect traffic to attacker-controlled servers."},

    {"question": "Why secure your home router with a strong admin password?",
     "options": [
         "Default or weak router credentials let attackers change settings or intercept traffic",
         "It speeds up the internet automatically",
         "It disables Wi-Fi",
         "It publishes your network publicly"
     ],
     "correct": 0,
     "explain": "Changing defaults prevents easy compromise of the network gateway."},

    {"question": "What is network segmentation used for?",
     "options": [
         "Separating networks to limit the scope of compromise and contain attacks",
         "Combining networks into one",
         "Publishing internal servers publicly",
         "Removing firewalls"
     ],
     "correct": 0,
     "explain": "Segmentation limits lateral movement and exposure."},

    {"question": "Why monitor network traffic for anomalies?",
     "options": [
         "To detect suspicious behaviors indicative of compromise or exfiltration",
         "To slow down the system",
         "To remove encryption",
         "To replace passwords"
     ],
     "correct": 0,
     "explain": "Traffic analysis helps identify attacks early and supports incident response."},

    {"question": "What is a man-in-the-middle attack?",
     "options": [
         "Attacker intercepts or alters communications between two parties",
         "A harmless routing update",
         "A backup process",
         "A firewall improvement"
     ],
     "correct": 0,
     "explain": "MITM allows attackers to eavesdrop or manipulate data if connections are not properly secured."},

    {"question": "Why change default SSID and admin credentials on wireless access points?",
     "options": [
         "Attackers often scan for default settings; changing them reduces exposure",
         "It speeds up devices",
         "It improves battery life",
         "It publishes passwords"
     ],
     "correct": 0,
     "explain": "Default settings are predictable and widely known; change them to increase security."},

    {"question": "What is a firewall's primary role?",
     "options": [
         "Control network traffic according to security rules to block unauthorized access",
         "Store passwords",
         "Encrypt disks",
         "Scan attachments"
     ],
     "correct": 0,
     "explain": "Firewalls limit exposure by filtering inbound and outbound traffic."},

    {"question": "Why use strong encryption for Wi-Fi (WPA2/WPA3)?",
     "options": [
         "To protect wireless traffic from eavesdropping and unauthorized access",
         "To increase signal strength",
         "To speed up the network always",
         "To allow public access"
     ],
     "correct": 0,
     "explain": "WPA2/WPA3 secure wireless traffic using encryption and authentication mechanisms."},

    {"question": "What is port scanning commonly used for by attackers?",
     "options": [
         "Finding open services to target",
         "Backing up systems",
         "Encrypting data",
         "Optimizing performance"
     ],
     "correct": 0,
     "explain": "Open ports reveal reachable services that may have vulnerabilities."},

    {"question": "Why use secure DNS services or DNS-over-HTTPS?",
     "options": [
         "To protect DNS queries from interception or manipulation",
         "To speed up downloads always",
         "To publish all of your addresses",
         "To replace firewalls"
     ],
     "correct": 0,
     "explain": "Securing DNS prevents attackers from hijacking or tampering with name resolution."},

    {"question": "What is a 'zero-day' vulnerability?",
     "options": [
         "A previously unknown flaw that attackers may exploit before a patch is available",
         "A scheduled backup",
         "An expired certificate",
         "A harmless system update"
     ],
     "correct": 0,
     "explain": "Zero-days are high-risk because there is no available vendor patch at discovery."},

    {"question": "Why use strong authentication for remote access (VPN/SSH)?",
     "options": [
         "To prevent unauthorized remote access and protect management channels",
         "To speed remote desktop",
         "To remove logging",
         "To publicize credentials"
     ],
     "correct": 0,
     "explain": "Secure remote access reduces risk of attackers entering internal networks."},

    {"question": "Why limit exposure of management interfaces to the public internet?",
     "options": [
         "Publicly exposed consoles are attractive targets and should be firewalled or restricted to known IPs",
         "They always need to be public",
         "They improve SEO",
         "They encrypt automatically"
     ],
     "correct": 0,
     "explain": "Restricting access reduces attack surface for admin functions."},

    {"question": "What is an IDS/IPS used for?",
     "options": [
         "Detecting (IDS) and optionally preventing (IPS) malicious network activity",
         "Backing up data",
         "Encrypting disks",
         "Replacing authentication"
     ],
     "correct": 0,
     "explain": "IDS/IPS provide monitoring and active defenses against network threats."},

    {"question": "Why rotate encryption keys periodically?",
     "options": [
         "To limit the amount of data exposed if a key is compromised",
         "To slow encryption",
         "To publish keys publicly",
         "To increase storage"
     ],
     "correct": 0,
     "explain": "Key rotation reduces the window of usefulness for stolen keys."},

    {"question": "What is the benefit of network flow logging?",
     "options": [
         "Provides historical traffic patterns for detection and investigation",
         "Deletes files automatically",
         "Speeds up flows always",
         "Removes encryption"
     ],
     "correct": 0,
     "explain": "Flows help identify anomalies and support incident analysis."},

    {"question": "Why apply least-privilege for network services?",
     "options": [
         "Services should run with minimum permissions to reduce damage if exploited",
         "To improve convenience only",
         "To expose services publicly",
         "To disable backups"
     ],
     "correct": 0,
     "explain": "Minimizing service privileges limits attacker capabilities after compromise."},

    {"question": "What is network hardening?",
     "options": [
         "Applying secure configurations, disabling unused services, and enforcing access controls",
         "Adding more user accounts",
         "Publishing network maps",
         "Installing random software"
     ],
     "correct": 0,
     "explain": "Hardening reduces potential vulnerabilities and misconfigurations that attackers exploit."},

    {"question": "Why segment guest Wi-Fi from corporate networks?",
     "options": [
         "To keep untrusted devices isolated and prevent lateral access to internal systems",
         "To increase guest speeds",
         "To share credentials",
         "To enable management access"
     ],
     "correct": 0,
     "explain": "Segregation prevents guest devices from accessing sensitive internal resources."},

    {"question": "What is threat intelligence used for in networks?",
     "options": [
         "Informing defenses about known indicators, emerging threats, and tactics",
         "Creating backups",
         "Increasing spam",
         "Eliminating logs"
     ],
     "correct": 0,
     "explain": "Threat intel enhances detection and proactive blocking of malicious activity."}
]

# ------------------------------------------------------------
# CATEGORY: Cryptography & Secure Protocols (30)
# ------------------------------------------------------------
crypto = [
    {"question": "What is the main purpose of encryption?",
     "options": [
         "Protect confidentiality and integrity of data by making it unreadable without a key",
         "Speed up systems",
         "Share passwords",
         "Block spam"
     ],
     "correct": 0,
     "explain": "Encryption ensures only authorized parties with keys can read protected data."},

    {"question": "What does TLS (used in HTTPS) provide?",
     "options": [
         "Encryption and authentication for communications between client and server",
         "Faster downloads always",
         "Public hosting",
         "Automatic backups"
     ],
     "correct": 0,
     "explain": "TLS secures communications by encrypting data and verifying server identity."},

    {"question": "What is asymmetric (public key) cryptography used for?",
     "options": [
         "Secure key exchange, digital signatures, and encrypting messages without shared secret",
         "Sharing passwords publicly",
         "Speeding up games",
         "Backing up files"
     ],
     "correct": 0,
     "explain": "Public/private key pairs enable secure operations where symmetric keys cannot be pre-shared."},

    {"question": "Why use strong key lengths and modern algorithms?",
     "options": [
         "To resist current cryptographic attacks and ensure long-term confidentiality",
         "To slow down everything",
         "To remove encryption",
         "To share keys publicly"
     ],
     "correct": 0,
     "explain": "Older or weak algorithms are vulnerable; use up-to-date standards and sufficient key sizes."},

    {"question": "What is a digital signature?",
     "options": [
         "A cryptographic proof that a message originated from a holder of a private key",
         "An email footer",
         "A password hint",
         "A firewall rule"
     ],
     "correct": 0,
     "explain": "Signatures verify authenticity and integrity of messages or files."},

    {"question": "Why protect private keys carefully?",
     "options": [
         "Compromise of private keys undermines all cryptographic guarantees and enables impersonation",
         "They are public by design",
         "They speed up encryption",
         "They are used for backups"
     ],
     "correct": 0,
     "explain": "Private keys must be stored securely to prevent unauthorized use."},

    {"question": "What is end-to-end encryption advantage?",
     "options": [
         "Only endpoints can decrypt message content, preventing intermediaries from reading it",
         "It speeds email",
         "It removes need for authentication",
         "It shares messages publicly"
     ],
     "correct": 0,
     "explain": "E2E protects content across transit and storage against intermediary access."},

    {"question": "Why use TLS certificates from trusted CAs?",
     "options": [
         "Trusted certificates allow browsers to validate server identity and avoid warning messages",
         "They make sites load faster",
         "They backup sites automatically",
         "They remove the need for passwords"
     ],
     "correct": 0,
     "explain": "Trusted CAs provide assurance that a site corresponds to a given domain."},

    {"question": "What is perfect forward secrecy (PFS)?",
     "options": [
         "A property where session keys cannot be retroactively decrypted even if long-term keys are compromised",
         "A backup method",
         "A firewall technique",
         "A spam filter"
     ],
     "correct": 0,
     "explain": "PFS protects past sessions from future key compromises via ephemeral key exchange."},

    {"question": "Why avoid storing sensitive data in plaintext?",
     "options": [
         "Plaintext is readable if storage is breached; sensitive data should be encrypted at rest",
         "Plaintext is always encrypted automatically",
         "Plaintext is required for performance",
         "Plaintext prevents backups"
     ],
     "correct": 0,
     "explain": "Encrypt at rest to protect stored data from unauthorized access."},

    {"question": "What is hashing used for?",
     "options": [
         "Creating a fixed-size digest for data integrity checks or password storage (with appropriate salts)",
         "Encrypting large files symmetrically",
         "Speeding networks",
         "Backing up keys"
     ],
     "correct": 0,
     "explain": "Hashing produces digests; salted slow hashes are used for secure password storage."},

    {"question": "Why salt passwords before hashing?",
     "options": [
         "To ensure identical passwords produce different hashes and resist rainbow table attacks",
         "To speed up cracking",
         "To publish hashes publicly",
         "To avoid hashing entirely"
     ],
     "correct": 0,
     "explain": "Salt adds randomness to each password hash, preventing precomputed attack lists."},

    {"question": "What is a certificate revocation list (CRL)?",
     "options": [
         "A list of certificates that should no longer be trusted because they were compromised or revoked",
         "A backup of certificates",
         "A firewall rule set",
         "A type of hash"
     ],
     "correct": 0,
     "explain": "CRLs and OCSP indicate certificates that are no longer valid and should not be trusted."},

    {"question": "Why use strong random number generators in cryptography?",
     "options": [
         "Predictable randomness weakens keys and undermines cryptographic security",
         "Randomness is irrelevant",
         "They speed up webpages",
         "They compress data"
     ],
     "correct": 0,
     "explain": "High-quality randomness is essential for generating secure keys and nonces."},

    {"question": "What is symmetric encryption?",
     "options": [
         "Encryption that uses the same key to encrypt and decrypt data",
         "Encryption using public/private key pairs",
         "A password manager",
         "A network protocol"
     ],
     "correct": 0,
     "explain": "Symmetric algorithms are efficient for large data but require secure key distribution."},

    {"question": "Why rotate encryption keys for long-lived data?",
     "options": [
         "To limit exposure if keys are compromised and reduce impact over time",
         "To make data public",
         "To remove encryption",
         "To slow systems intentionally"
     ],
     "correct": 0,
     "explain": "Key rotation reduces the amount of data vulnerable to compromised keys."},

    {"question": "What is an HSM (hardware security module) used for?",
     "options": [
         "Securely generating, storing, and protecting cryptographic keys in hardware",
         "Backing up databases",
         "Publishing keys publicly",
         "Scanning for malware"
     ],
     "correct": 0,
     "explain": "HSMs provide strong physical and logical protection for sensitive keys."},

    {"question": "What is a TLS downgrade attack?",
     "options": [
         "Forcing a connection to use older, weaker protocol versions or ciphers",
         "Upgrading TLS to the latest",
         "Publishing certificates",
         "Backing up keys"
     ],
     "correct": 0,
     "explain": "Downgrades exploit compatibility to reduce security; servers should disable weak protocols."},

    {"question": "Why validate certificates and chain of trust?",
     "options": [
         "To ensure the certificate came from a trusted authority and was issued for the correct domain",
         "To speed browsing",
         "To compress data",
         "To eliminate logs"
     ],
     "correct": 0,
     "explain": "Certificate validation confirms authenticity and prevents impersonation."},

    {"question": "What is key escrow and why is it controversial?",
     "options": [
         "A mechanism to store keys for recovery which may introduce trust and privacy concerns",
         "A backup system always recommended",
         "A firewall setting",
         "An encryption algorithm"
     ],
     "correct": 0,
     "explain": "Escrow can help recovery but creates risks if escrow is compromised or misused."},

    {"question": "What is 'cryptographic agility'?",
     "options": [
         "Ability to switch cryptographic algorithms or parameters as attacks evolve",
         "Using fixed algorithms forever",
         "Publishing keys publicly",
         "Removing encryption"
     ],
     "correct": 0,
     "explain": "Agility allows systems to adopt stronger algorithms when needed."},

    {"question": "Why avoid rolling your own cryptography?",
     "options": [
         "Designing secure cryptography is error-prone; use vetted libraries and standards",
         "It is always better",
         "It makes systems faster",
         "It improves backup processes"
     ],
     "correct": 0,
     "explain": "Standard, peer-reviewed implementations reduce risk of subtle security bugs."},

    {"question": "What is data integrity checking?",
     "options": [
         "Verifying data has not been altered using hashes or signatures",
         "Encrypting files only",
         "Backing up data automatically",
         "Deleting logs"
     ],
     "correct": 0,
     "explain": "Integrity checks detect tampering or corruption of data."},

    {"question": "Why store only hashed password digests, not plaintext?",
     "options": [
         "Plaintext exposure allows immediate account takeover; hashed digests reduce impact if stored securely",
         "Hashed digests are readable by everyone",
         "Plaintext is safer",
         "Hashing compresses data"
     ],
     "correct": 0,
     "explain": "Secure hashing practices limit damage when database breaches occur."}
]

# ------------------------------------------------------------
# CATEGORY: Secure Software Practices (30)
# ------------------------------------------------------------
secure_software = [
    {"question": "What is input validation in secure coding?",
     "options": [
         "Checking and sanitizing user input to prevent injection and unexpected behavior",
         "Allowing any input freely",
         "Compressing data",
         "Removing logs"
     ],
     "correct": 0,
     "explain": "Validating input prevents attackers from injecting malicious payloads like SQL or command injection."},

    {"question": "What is an SQL injection?",
     "options": [
         "Injection of malicious SQL through unvalidated inputs to manipulate a database",
         "A type of encryption",
         "A network scanning method",
         "A browser plugin"
     ],
     "correct": 0,
     "explain": "SQLi exploits improper handling of inputs in database queries to read or modify data."},

    {"question": "Why use parameterized queries or prepared statements?",
     "options": [
         "They separate code and data, preventing injection attacks like SQLi",
         "They speed up the UI only",
         "They remove the need for authentication",
         "They are deprecated"
     ],
     "correct": 0,
     "explain": "Parameterized queries ensure user input cannot change query structure."},

    {"question": "What is cross-site scripting (XSS)?",
     "options": [
         "Injection of malicious scripts into web pages viewed by other users",
         "A firewall technique",
         "A backup method",
         "A network protocol"
     ],
     "correct": 0,
     "explain": "XSS allows attackers to run scripts in victims' browsers to steal session data or perform actions."},

    {"question": "How to mitigate XSS?",
     "options": [
         "Encode output and use strict input handling and Content Security Policy (CSP)",
         "Allow all user HTML",
         "Store passwords in plaintext",
         "Disable logging"
     ],
     "correct": 0,
     "explain": "Output encoding and CSP reduce the risk of injected scripts executing."},

    {"question": "What is secure session management?",
     "options": [
         "Properly generating, storing, and expiring session tokens to prevent hijacking",
         "Sharing session IDs publicly",
         "Using predictable tokens",
         "Never expiring tokens"
     ],
     "correct": 0,
     "explain": "Sessions should be protected against fixation and interception."},

    {"question": "Why follow the principle of least privilege in code execution?",
     "options": [
         "Limit code and processes to minimal rights to reduce damage from a compromise",
         "Grant all rights to speed development",
         "Share permissions across services",
         "Remove error handling"
     ],
     "correct": 0,
     "explain": "Least privilege minimizes the impact if a component is exploited."},

    {"question": "What is dependency management for security?",
     "options": [
         "Keeping libraries and dependencies up-to-date and tracking vulnerabilities",
         "Ignoring library versions",
         "Installing all packages without review",
         "Publishing libraries publicly"
     ],
     "correct": 0,
     "explain": "Outdated dependencies can contain known vulnerabilities; management prevents avoidable risk."},

    {"question": "What is threat modeling?",
     "options": [
         "Analyzing a system to identify potential threats and mitigation strategies",
         "Only writing tests",
         "Formatting code",
         "Removing logs"
     ],
     "correct": 0,
     "explain": "Threat modeling anticipates attacker techniques and helps design defenses."},

    {"question": "Why use secure defaults in software?",
     "options": [
         "Default configurations should favor security because many users do not change settings",
         "Defaults should be as permissive as possible",
         "Defaults always reduce security",
         "Defaults remove authentication"
     ],
     "correct": 0,
     "explain": "Secure defaults reduce misconfiguration risk for end users."},

    {"question": "What is code review for security?",
     "options": [
         "Examining code for logic, vulnerabilities, and insecure constructs before production",
         "Only checking spelling",
         "Removing comments",
         "Automating backups"
     ],
     "correct": 0,
     "explain": "Reviews help find security defects early when they are cheaper to fix."},

    {"question": "Why validate authorization on the server side?",
     "options": [
         "Client-side checks can be bypassed; server must enforce access control reliably",
         "Client-side checks are always secure",
         "Server-side checks slow everything down",
         "Client-side checks are unnecessary"
     ],
     "correct": 0,
     "explain": "Trust on the client is unreliable; servers must enforce permissions."},

    {"question": "What is secure configuration management?",
     "options": [
         "Maintaining consistent, hardened configuration across environments and tracking changes",
         "Randomly setting options",
         "Publishing keys publicly",
         "Disabling logs"
     ],
     "correct": 0,
     "explain": "Controlled configurations reduce misconfigurations that attackers exploit."},

    {"question": "Why sanitize file uploads?",
     "options": [
         "To prevent executable content or dangerous filenames from being processed",
         "To always accept everything",
         "To compress images",
         "To publish uploads publicly"
     ],
     "correct": 0,
     "explain": "Sanitization prevents filename traversal and execution of uploaded code."},

    {"question": "What is secure logging practice?",
     "options": [
         "Log necessary events for detection but avoid storing sensitive data like full passwords",
         "Log everything including secrets",
         "Never log anything",
         "Publish logs publicly"
     ],
     "correct": 0,
     "explain": "Logging supports detection while protecting sensitive information from exposure."},

    {"question": "Why implement rate limiting?",
     "options": [
         "To reduce brute-force and abuse by limiting requests from clients",
         "To allow unlimited login attempts",
         "To speed up attacks",
         "To remove authentication"
     ],
     "correct": 0,
     "explain": "Rate limits slow attack attempts and protect resources."},

    {"question": "What is secure error handling?",
     "options": [
         "Return helpful but non-sensitive messages and record details in logs for analysis",
         "Display full stack traces to users",
         "Ignore all errors silently",
         "Publish errors publicly"
     ],
     "correct": 0,
     "explain": "Avoid exposing internal details to users while keeping records for debugging."},

    {"question": "Why limit CORS origins in web apps?",
     "options": [
         "To restrict which origins can interact with your API and reduce cross-site risks",
         "To allow any origin for convenience",
         "To improve caching always",
         "To remove headers"
     ],
     "correct": 0,
     "explain": "Restrictive CORS prevents arbitrary sites from making authenticated requests."},

    {"question": "What is secure secret management?",
     "options": [
         "Storing API keys and credentials in protected vaults rather than in code or public repos",
         "Committing secrets to source control",
         "Sending keys via email",
         "Posting keys in public channels"
     ],
     "correct": 0,
     "explain": "Vaults and environment-based injection reduce accidental secret leakage."},

    {"question": "Why use automated testing for security (SAST/DAST)?",
     "options": [
         "To identify vulnerabilities early and continuously during development",
         "To replace human reviewers entirely",
         "To slow deployment only",
         "To publish tests publicly"
     ],
     "correct": 0,
     "explain": "Static and dynamic testing find classes of vulnerabilities that might otherwise go unnoticed."},

    {"question": "What is dependency scanning?",
     "options": [
         "Checking third-party libraries for known vulnerabilities and licensing issues",
         "Installing all dependencies automatically",
         "Ignoring versions",
         "Publishing them publicly"
     ],
     "correct": 0,
     "explain": "Scanning prevents use of libraries with known security flaws."},

    {"question": "Why perform security-focused penetration testing?",
     "options": [
         "To simulate attacker tactics and identify real-world exploitable weaknesses",
         "To slow development",
         "To confuse teams",
         "To compress code"
     ],
     "correct": 0,
     "explain": "Pen tests reveal practical gaps that automated tools might miss."},

    {"question": "What is secure build pipeline practice?",
     "options": [
         "Ensure builds run in controlled environments, use signed artifacts, and prevent tampering",
         "Build on any developer machine unrestricted",
         "Publish build keys publicly",
         "Remove code signing"
     ],
     "correct": 0,
     "explain": "Secure pipelines protect software integrity from source to production."},

    {"question": "Why apply the principle of defense-in-depth in software design?",
     "options": [
         "Multiple layers of controls reduce chance that a single failure leads to compromise",
         "One control is always sufficient",
         "To add complexity only",
         "To publish all controls publicly"
     ],
     "correct": 0,
     "explain": "Layering controls increases resilience against different attack vectors."}
]

# ------------------------------------------------------------
# CATEGORY: Incident Response & Monitoring (30)
# ------------------------------------------------------------
incident_response = [
    {"question": "What is the first step when you suspect an active security incident?",
     "options": [
         "Contain the affected systems, preserve evidence, and follow incident response procedures",
         "Delete logs immediately",
         "Share credentials to fix it",
         "Ignore and continue working"
     ],
     "correct": 0,
     "explain": "Containment and preservation are critical to stop damage and support investigation."},

    {"question": "Why preserve forensic evidence?",
     "options": [
         "To understand the scope and cause of an incident and support legal or recovery actions",
         "To delete it later",
         "To speed up systems",
         "To share publicly"
     ],
     "correct": 0,
     "explain": "Preservation allows investigators to analyze what happened and prevents loss of critical data."},

    {"question": "What is a playbook in IR?",
     "options": [
         "A documented set of steps and roles for responding to specific incident types",
         "A music playlist",
         "A backup schedule",
         "A firewall rule"
     ],
     "correct": 0,
     "explain": "Playbooks provide repeatable, tested procedures for consistent incident response."},

    {"question": "Why have a communication plan during incidents?",
     "options": [
         "To coordinate internal and external messaging, legal obligations, and minimize panic",
         "To publish all details immediately",
         "To avoid notifying anyone",
         "To post on social media first"
     ],
     "correct": 0,
     "explain": "Planned communications help manage reputational and legal risks during incidents."},

    {"question": "What is detection tuning?",
     "options": [
         "Adjusting alerts and rules to reduce noise and focus on meaningful threats",
         "Turning off all monitoring",
         "Publishing alerts publicly",
         "Disabling logs"
     ],
     "correct": 0,
     "explain": "Tuning improves signal-to-noise, enabling faster response to true positives."},

    {"question": "Why maintain an incident response team and roles?",
     "options": [
         "Clear responsibilities enable coordinated, efficient response and recovery",
         "So no one is accountable",
         "To slow decision-making always",
         "To remove backups"
     ],
     "correct": 0,
     "explain": "Predefined roles reduce confusion and speed up critical actions during incidents."},

    {"question": "What is threat hunting?",
     "options": [
         "Proactive searching for hidden threats within environments using hypotheses and telemetry",
         "A backup job",
         "A firewall technique only",
         "A developer task"
     ],
     "correct": 0,
     "explain": "Hunting finds adversary activity that automated detection may miss."},

    {"question": "Why test your incident response plans?",
     "options": [
         "To ensure procedures work, roles are clear, and gaps are discovered and fixed",
         "To avoid training",
         "To publish plans publicly",
         "To disable monitoring"
     ],
     "correct": 0,
     "explain": "Exercises reveal weaknesses and prepare teams for real events."},

    {"question": "What is containment in IR?",
     "options": [
         "Actions that limit the spread and impact of a compromise while preserving evidence",
         "Reinstalling the OS only",
         "Backing up everything",
         "Deleting user accounts permanently"
     ],
     "correct": 0,
     "explain": "Containment aims to isolate affected systems and prevent further damage."},

    {"question": "Why maintain an inventory of assets?",
     "options": [
         "Knowing hardware and software assets helps prioritize protection and respond to incidents",
         "To increase complexity only",
         "To publish asset lists",
         "To remove logs"
     ],
     "correct": 0,
     "explain": "Asset inventories support risk assessment and faster incident triage."},

    {"question": "What is 'root cause analysis' after an incident?",
     "options": [
         "Investigating the underlying reasons for the incident to prevent recurrence",
         "A random task",
         "A backup technique",
         "A firewall update"
     ],
     "correct": 0,
     "explain": "Understanding root causes leads to remediation and stronger controls."},

    {"question": "Why keep backups and test restores as part of IR?",
     "options": [
         "Backups enable recovery from destructive attacks and should be tested to ensure usability",
         "Backups are unnecessary",
         "Backups always fail",
         "Backups expose sensitive data"
     ],
     "correct": 0,
     "explain": "Regular restore tests verify that backups are reliable in an incident."},

    {"question": "What is blast radius reduction?",
     "options": [
         "Designing systems to limit the impact of a compromise through segmentation and least privilege",
         "Increasing attack surface",
         "Sharing admin rights widely",
         "Publishing keys"
     ],
     "correct": 0,
     "explain": "Reducing blast radius confines breaches and simplifies recovery."},

    {"question": "Why perform post-incident reviews?",
     "options": [
         "To learn lessons, document improvements, and update controls and playbooks",
         "To ignore the incident afterwards",
         "To delete logs permanently",
         "To publish sensitive data"
     ],
     "correct": 0,
     "explain": "Reviews help organizations strengthen posture and prevent similar incidents."},

    {"question": "What is the purpose of telemetry and centralized logging?",
     "options": [
         "Provide visibility into system events for detection and forensic analysis",
         "To slow systems",
         "To remove monitoring",
         "To backup everything automatically"
     ],
     "correct": 0,
     "explain": "Centralized logs enable correlation, detection, and investigation across systems."},

    {"question": "Why maintain a contact list for incident response?",
     "options": [
         "To quickly reach internal roles, vendors, and external responders during incidents",
         "To publish contacts publicly",
         "To share passwords",
         "To avoid communication"
     ],
     "correct": 0,
     "explain": "Fast coordination with the right parties reduces response time."},

    {"question": "What is 'containment vs eradication' distinction?",
     "options": [
         "Containment limits impact immediately; eradication removes the threat fully before recovery",
         "They mean the same thing",
         "Both involve backing up logs only",
         "Both are unrelated to IR"
     ],
     "correct": 0,
     "explain": "Containment is immediate damage control; eradication fixes the root cause for recovery."},

    {"question": "Why preserve chain-of-custody for evidence?",
     "options": [
         "Ensure forensic integrity and admissibility for legal or investigative use",
         "Because logs are never useful",
         "Because chain-of-custody speeds up systems",
         "Because it removes backups"
     ],
     "correct": 0,
     "explain": "Documenting who handled evidence prevents contamination and supports legal processes."},

    {"question": "What is continuous monitoring?",
     "options": [
         "Ongoing collection and analysis of security telemetry to detect and respond to threats",
         "A one-time scan only",
         "A backup process",
         "A firewall update"
     ],
     "correct": 0,
     "explain": "Continuous monitoring enables timely detection and reduces dwell time for attackers."},

    {"question": "Why classify incidents by severity?",
     "options": [
         "To prioritize response and allocate resources effectively based on impact",
         "To delay all responses equally",
         "To publish incidents publicly",
         "To remove logs"
     ],
     "correct": 0,
     "explain": "Severity classification focuses attention and resources where they matter most."},

    {"question": "What is an SLA in incident response context?",
     "options": [
         "A service-level agreement or internal target defining response and remediation timelines",
         "A backup schedule",
         "A software license",
         "A firewall rule"
     ],
     "correct": 0,
     "explain": "SLAs set expectations for detection and response speed."},

    {"question": "Why maintain 'lessons learned' and implement improvements?",
     "options": [
         "To close gaps discovered during incidents and strengthen controls",
         "To forget about incidents quickly",
         "To publish sensitive data",
         "To remove monitoring"
     ],
     "correct": 0,
     "explain": "Applying lessons reduces recurrence and improves resilience."},

    {"question": "What is 'dwell time'?",
     "options": [
         "The time an attacker remains undetected inside a network",
         "The time to backup files",
         "The hardware lifetime",
         "The time to install antivirus"
     ],
     "correct": 0,
     "explain": "Shorter dwell time limits attacker impact and exfiltration opportunities."},

    {"question": "Why run tabletop exercises for IR teams?",
     "options": [
         "To practice scenarios, clarify roles, and find process gaps without production impact",
         "To replace playbooks",
         "To publish data publicly",
         "To disable monitoring"
     ],
     "correct": 0,
     "explain": "Tabletop exercises test coordination and decision-making before real incidents."},

    {"question": "What is escalation in IR?",
     "options": [
         "Moving an incident to higher expertise or management when its complexity or impact requires it",
         "Deleting logs",
         "Ignoring tickets",
         "Publishing passwords"
     ],
     "correct": 0,
     "explain": "Escalation gets appropriate expertise and authority for complex incidents."}
]

# ------------------------------------------------------------
# CATEGORY: Device Security (30)
# ------------------------------------------------------------
device_security = [
    {"question": "Why lock your computer or phone when not in use?",
     "options": [
         "To prevent someone nearby from accessing your session and data",
         "To make the screen prettier",
         "To improve battery life",
         "To speed up downloads"
     ],
     "correct": 0,
     "explain": "Lock screens protect against opportunistic physical access."},

    {"question": "Why enable device encryption?",
     "options": [
         "Protects data at rest so if the device is lost or stolen, data cannot be read without keys",
         "It speeds device performance",
         "It disables screen locking",
         "It shares keys publicly"
     ],
     "correct": 0,
     "explain": "Encryption prevents unauthorized access to stored data on lost or stolen devices."},

    {"question": "Why keep devices updated?",
     "options": [
         "To receive security patches that fix vulnerabilities attackers exploit",
         "To change wallpapers",
         "To share passwords easily",
         "To remove logs"
     ],
     "correct": 0,
     "explain": "Updates address known flaws and reduce the likelihood of compromise."},

    {"question": "What is remote wipe useful for?",
     "options": [
         "Erasing data on a lost or stolen device to protect sensitive information",
         "Installing new apps",
         "Increasing storage",
         "Publishing contacts"
     ],
     "correct": 0,
     "explain": "Remote wipe limits exposure when devices cannot be recovered."},

    {"question": "Why use biometric or strong PIN locks?",
     "options": [
         "They make device access harder for an attacker with physical access",
         "They always slow the device",
         "They are required for backups",
         "They remove encryption"
     ],
     "correct": 0,
     "explain": "Strong authentication on devices reduces unauthorized local access."},

    {"question": "Why avoid jailbreaking or rooting devices for general use?",
     "options": [
         "It removes vendor protections and may introduce vulnerabilities or instability",
         "It always improves security",
         "It automatically updates firmware",
         "It encrypts files better"
     ],
     "correct": 0,
     "explain": "Rooted devices lose built-in security controls and are more vulnerable to malware."},

    {"question": "Why disable Bluetooth and Wi-Fi when unused on mobile devices?",
     "options": [
         "To reduce exposure to network-based attacks and accidental pairing",
         "To increase battery life only",
         "To prevent software updates",
         "To allow others to connect freely"
     ],
     "correct": 0,
     "explain": "Disabling radios reduces the attack surface of nearby connections."},

    {"question": "Why use strong passwords on device accounts (not just apps)?",
     "options": [
         "Device compromise can expose multiple accounts and data if unlocked with weak credentials",
         "Device passwords are irrelevant",
         "They speed up the device",
         "They publish data publicly"
     ],
     "correct": 0,
     "explain": "Device-level protection prevents access to all local data and accounts."},

    {"question": "What is mobile device management (MDM)?",
     "options": [
         "A system for centrally managing, configuring, and securing corporate mobile devices",
         "A malware scanner only",
         "A backup for all apps",
         "A social app"
     ],
     "correct": 0,
     "explain": "MDM enforces policies, deploys configs, and can wipe or lock devices remotely."},

    {"question": "Why avoid installing apps from unknown stores on mobile devices?",
     "options": [
         "Third-party stores may host malicious or tampered applications",
         "They are always faster",
         "They improve battery life",
         "They automatically encrypt data"
     ],
     "correct": 0,
     "explain": "Stick to official app stores to reduce risk of malicious apps."},

    {"question": "Why set screens to auto-lock quickly?",
     "options": [
         "To reduce the window an unattended device is accessible by others",
         "To increase screen brightness",
         "To publish device info",
         "To remove locks"
     ],
     "correct": 0,
     "explain": "Short auto-lock reduces exposure from forgotten or idle devices."},

    {"question": "Why avoid connecting unknown USB drives to devices?",
     "options": [
         "They may contain malware that executes upon connection",
         "They always help backups",
         "They improve performance",
         "They clean the system"
     ],
     "correct": 0,
     "explain": "USB devices can be vectors for malware; scan and avoid unknown media."},

    {"question": "What is application sandboxing on devices?",
     "options": [
         "Isolating apps so their data and actions are confined and cannot affect others easily",
         "Sharing data across apps automatically",
         "Removing security checks",
         "Publishing app data publicly"
     ],
     "correct": 0,
     "explain": "Sandboxes reduce app-level risk by restricting permissions and access."},

    {"question": "Why backup mobile data regularly?",
     "options": [
         "To recover contacts, photos and data after loss, theft, or ransomware",
         "To increase vulnerability",
         "To publish data online",
         "To remove encryption"
     ],
     "correct": 0,
     "explain": "Backups allow recovery independent of a compromised or lost device."},

    {"question": "Why disable 'automatic join' of open Wi-Fi networks?",
     "options": [
         "To avoid connecting to malicious hotspots and exposing traffic",
         "To speed up browsing",
         "To make networks public",
         "To remove encryption"
     ],
     "correct": 0,
     "explain": "Manual selection reduces risk of automatically joining unsafe networks."},

    {"question": "What is firmware and why update it?",
     "options": [
         "Low-level device software that may contain security fixes; keeping it patched reduces hardware-level vulnerabilities",
         "A backup file",
         "A user document",
         "A browser plugin"
     ],
     "correct": 0,
     "explain": "Firmware updates fix vulnerabilities that attackers can exploit at the device level."},

    {"question": "Why protect BIOS/UEFI with passwords and secure boot?",
     "options": [
         "To prevent tampering with boot process and unauthorized low-level modifications",
         "To speed up boot times only",
         "To remove startup screens",
         "To publish settings publicly"
     ],
     "correct": 0,
     "explain": "Secure boot and firmware protections help prevent persistent compromise below the OS."},

    {"question": "Why use trusted chargers and cables?",
     "options": [
         "Malicious charging cables or chargers can attempt data transfer or malware delivery; use trusted accessories",
         "They always improve speed",
         "They are required by law",
         "They remove the need for passwords"
     ],
     "correct": 0,
     "explain": "Use manufacturer-approved accessories to avoid hidden data channels or tampering."},

    {"question": "What is a device attestation?",
     "options": [
         "A proof that a device is in a known secure state before granting access to sensitive services",
         "A backup policy",
         "A public listing of devices",
         "A firewall rule"
     ],
     "correct": 0,
     "explain": "Attestation helps ensure only trusted devices access critical systems."},

    {"question": "Why set up Find My Device / similar services?",
     "options": [
         "To locate, lock, or remotely wipe lost or stolen devices to protect data",
         "To speed up devices",
         "To publish location publicly",
         "To disable backups"
     ],
     "correct": 0,
     "explain": "Remote management limits exposure when devices are lost."},

    {"question": "Why avoid using developer or debug modes on production devices?",
     "options": [
         "They can weaken protections and expose diagnostic endpoints attackers may use",
         "They increase encryption",
         "They always improve security",
         "They remove logs"
     ],
     "correct": 0,
     "explain": "Disable or secure debug modes to prevent unintended access to internals."},

    {"question": "Why protect biometric templates and allow fallback PINs cautiously?",
     "options": [
         "Biometric data must remain private; fallback authentication should be strong because biometrics cannot be changed if compromised",
         "Biometrics always replace passwords fully",
         "Biometric data is public by design",
         "Fallback PINs should be simple"
     ],
     "correct": 0,
     "explain": "Treat biometric data and fallback methods with strong protections and policies."},

    {"question": "What is remote attestation?",
     "options": [
         "A process where hardware or software proves its integrity to remote services before access",
         "A backup procedure",
         "A logging setting",
         "A firewall configuration"
     ],
     "correct": 0,
     "explain": "Remote attestation verifies device trustworthiness prior to granting sensitive access."},

    {"question": "Why disable unused services and ports on devices?",
     "options": [
         "To reduce the attack surface and fewer potential entry points for attackers",
         "To increase complexity only",
         "To publish ports publicly",
         "To remove logs"
     ],
     "correct": 0,
     "explain": "Fewer running services means fewer vulnerabilities to exploit."}
]

# ------------------------------------------------------------
# CATEGORY: Cyber Ethics & Privacy (30)
# ------------------------------------------------------------
cyber_ethics = [
    {"question": "Why is cyber ethics important?",
     "options": [
         "It promotes lawful and respectful behavior online to protect rights and privacy",
         "It encourages hacking others",
         "It forces sharing passwords",
         "It removes laws"
     ],
     "correct": 0,
     "explain": "Ethical behavior maintains trust, privacy, and legal compliance in digital spaces."},

    {"question": "Why protect privacy of other people's data?",
     "options": [
         "Sharing private data without consent can harm individuals and violate laws",
         "It improves performance",
         "It speeds websites",
         "It is required for backups"
     ],
     "correct": 0,
     "explain": "Respecting privacy prevents harm and legal exposure."},

    {"question": "What does responsible disclosure mean?",
     "options": [
         "Reporting security vulnerabilities to the owner first and allowing time for fix before public disclosure",
         "Publishing vulnerabilities immediately without notice",
         "Ignoring discovered bugs",
         "Selling exploits publicly"
     ],
     "correct": 0,
     "explain": "Responsible disclosure balances public safety and gives owners time to patch issues."},

    {"question": "Why avoid distributing pirated software?",
     "options": [
         "Pirated software often includes malware and violates copyright laws",
         "It increases security",
         "It is always safe",
         "It is required for learning"
     ],
     "correct": 0,
     "explain": "Use licensed software to get updates and avoid malicious modifications."},

    {"question": "What is data minimization?",
     "options": [
         "Collecting only the necessary personal data to reduce risk and protect privacy",
         "Collecting as much data as possible",
         "Publishing customer data",
         "Ignoring consent"
     ],
     "correct": 0,
     "explain": "Limiting data reduces exposure and compliance burdens."},

    {"question": "Why consider fairness and bias in algorithms?",
     "options": [
         "To avoid discriminatory outcomes and protect user rights when using automated decisions",
         "To remove security",
         "To publish biased results",
         "To speed up computation only"
     ],
     "correct": 0,
     "explain": "Ethical design ensures systems do not harm or unfairly treat groups."},

    {"question": "What is GDPR / data protection principle relevance to security?",
     "options": [
         "Regulations require appropriate technical and organizational measures to protect personal data",
         "They focus only on marketing",
         "They remove encryption requirements",
         "They only apply to backups"
     ],
     "correct": 0,
     "explain": "Legal frameworks mandate protections and breach notification obligations for personal data."},

    {"question": "Why avoid collecting unnecessary personal identifiers?",
     "options": [
         "Extra data increases risk and obligation to protect it",
         "It always improves personalization",
         "It speeds up processing",
         "It is required by default"
     ],
     "correct": 0,
     "explain": "Collect less data to reduce potential privacy harm and compliance burden."},

    {"question": "What is informed consent regarding data?",
     "options": [
         "Users should be told what data is collected and how it is used and give consent knowingly",
         "Consent can be assumed always",
         "Consent is not required for personal data",
         "Consent allows unlimited sharing"
     ],
     "correct": 0,
     "explain": "Transparent practices respect user autonomy and legal obligations."},

    {"question": "Why anonymize data where possible?",
     "options": [
         "To enable analytics while protecting individual identities and reducing privacy risk",
         "To make data public always",
         "To prevent backups",
         "To increase attack surface"
     ],
     "correct": 0,
     "explain": "Anonymization reduces the impact if data is exposed."},

    {"question": "What is the ethical problem with mass surveillance without oversight?",
     "options": [
         "It can infringe on privacy rights and enable abuse if unchecked",
         "It always improves security",
         "It is required by all laws",
         "It is harmless"
     ],
     "correct": 0,
     "explain": "Oversight and legal frameworks are needed to balance security and civil liberties."},

    {"question": "Why disclose incidents to affected users responsibly?",
     "options": [
         "To allow them to take protective measures and satisfy legal notification requirements",
         "To hide the incident always",
         "To post data publicly",
         "To avoid responsibility"
     ],
     "correct": 0,
     "explain": "Timely notification helps users mitigate harm and complies with regulations."},

    {"question": "Why assess privacy impact for new projects?",
     "options": [
         "To identify risks to individuals and design mitigations before deployment",
         "To avoid thinking about privacy",
         "To publish all data",
         "To speed development only"
     ],
     "correct": 0,
     "explain": "Privacy impact assessments guide safer and lawful system design."},

    {"question": "What is ethical use of penetration testing?",
     "options": [
         "Only with authorization and rules of engagement to avoid harm and legal issues",
         "Testing randomly on the internet",
         "Selling exploits publicly",
         "Scattering malware for research"
     ],
     "correct": 0,
     "explain": "Authorized testing prevents unintended damage and legal exposure."},

    {"question": "Why protect children's data specially?",
     "options": [
         "Children have additional privacy protections and increased vulnerability, requiring special care",
         "Children's data is always public",
         "Children don't require protection",
         "Children's data is irrelevant"
     ],
     "correct": 0,
     "explain": "Extra safeguards and consent rules apply to minors in many jurisdictions."},

    {"question": "Why follow licensing and copyright when using software or data?",
     "options": [
         "Respecting rights prevents legal issues and ensures proper use and attribution",
         "Licenses are optional always",
         "It is safe to ignore licenses",
         "Licenses expose data publicly"
     ],
     "correct": 0,
     "explain": "Complying with licenses avoids legal risk and respects creators."},

    {"question": "Why avoid doxxing or sharing others' personal details without consent?",
     "options": [
         "It can cause real-world harm and legal consequences",
         "It is always harmless",
         "It improves security",
         "It is required by law"
     ],
     "correct": 0,
     "explain": "Doxxing violates privacy and puts people at risk of harassment or worse."},

    {"question": "What is an ethical consideration for AI in security?",
     "options": [
         "Ensure transparency, fairness, and accountability in automated decisions",
         "Always deploy without testing",
         "Ignore bias",
         "Publish training data without review"
     ],
     "correct": 0,
     "explain": "Ethical AI design reduces bias and unintended harm in security contexts."},

    {"question": "Why anonymize or redact PII in logs where possible?",
     "options": [
         "To protect personal data while retaining useful telemetry for security",
         "To make logs unreadable always",
         "To publish logs publicly",
         "To remove all monitoring"
     ],
     "correct": 0,
     "explain": "Redaction balances privacy and operational needs."},

    {"question": "Why follow data retention policies?",
     "options": [
         "To limit how long personal data is stored and reduce exposure risk",
         "To keep everything forever",
         "To publish data publicly",
         "To remove backups"
     ],
     "correct": 0,
     "explain": "Retention policies manage legal, privacy, and storage trade-offs."},

    {"question": "What is responsible automation in security?",
     "options": [
         "Automating repetitive tasks carefully with human oversight for decision points",
         "Automating everything without checks",
         "Removing humans entirely",
         "Publishing all automation scripts"
     ],
     "correct": 0,
     "explain": "Automation improves efficiency but requires oversight to avoid unintended consequences."},

    {"question": "Why keep transparency about data usage in privacy notices?",
     "options": [
         "Users deserve to know how their data is used and have choices about it",
         "Transparency reduces trust",
         "Privacy notices should be hidden",
         "Notices improve spam"
     ],
     "correct": 0,
     "explain": "Clear notices support informed consent and compliance."},

    {"question": "Why consider accessibility and equal access in cybersecurity tools?",
     "options": [
         "Security measures should be usable by people with disabilities to avoid exclusion",
         "Only able-bodied users matter",
         "Accessibility reduces security",
         "Accessibility is unrelated"
     ],
     "correct": 0,
     "explain": "Inclusive design ensures security protections are practical for all users."},

    {"question": "Why avoid sharing test or production data with third parties unnecessarily?",
     "options": [
         "It increases exposure risk and potential privacy breaches",
         "It always improves performance",
         "It reduces legal complexity",
         "It is required for security"
     ],
     "correct": 0,
     "explain": "Limit data sharing to minimize potential misuse or leakage."}
]

# ------------------------------------------------------------
# CATEGORY: Security Awareness & Policy (30)
# ------------------------------------------------------------
security_awareness = [
    {"question": "Why implement a security awareness program?",
     "options": [
         "To teach staff to recognize threats and follow safe practices that reduce human risk",
         "To punish users for mistakes",
         "To ignore phishing",
         "To remove all technology"
     ],
     "correct": 0,
     "explain": "Awareness programs reduce human-mediated compromises and encourage reporting."},

    {"question": "Why have clear acceptable use policies?",
     "options": [
         "Provide users rules for proper use of systems and consequences for misuse",
         "To allow unrestricted use",
         "To remove access controls",
         "To publish passwords"
     ],
     "correct": 0,
     "explain": "Policies set expectations and support enforcement of security standards."},

    {"question": "What is social engineering simulation?",
     "options": [
         "Controlled phishing tests to measure and improve user vigilance and training",
         "Random spamming of employees",
         "Publishing accounts publicly",
         "Removing training entirely"
     ],
     "correct": 0,
     "explain": "Simulations educate users and identify areas needing further training."},

    {"question": "Why make incident reporting easy and non-punitive?",
     "options": [
         "Encourage timely reporting so threats are addressed quickly without fear of blame",
         "To hide incidents",
         "To punish reporters",
         "To avoid taking action"
     ],
     "correct": 0,
     "explain": "Reporting supports quick containment and learning; punitive cultures deter reporting."},

    {"question": "Why align policies with legal and regulatory requirements?",
     "options": [
         "To ensure compliance and reduce legal risk while protecting data subjects",
         "To avoid doing any security",
         "To publish data publicly",
         "To ignore laws"
     ],
     "correct": 0,
     "explain": "Compliance ensures organizational practices meet legal obligations for data and security."},

    {"question": "What is acceptable use for removable media?",
     "options": [
         "Use only approved, scanned media and avoid unknown USB drives",
         "Plug any found USB into corporate machines",
         "Use USBs from public places freely",
         "Distribute unknown media to staff"
     ],
     "correct": 0,
     "explain": "Controlled removable media use prevents malware infections and data leakage."},

    {"question": "Why encourage reporting suspicious messages and incidents?",
     "options": [
         "Reporting enables defenders to block threats and alert others before scams spread",
         "Reporting is pointless",
         "Reporting must be public",
         "Reporting should be ignored"
     ],
     "correct": 0,
     "explain": "Early reporting reduces impact and supports protective measures."},

    {"question": "Why run regular security awareness refreshers?",
     "options": [
         "To keep knowledge current and reinforce safe behaviors against evolving threats",
         "To punish staff repeatedly",
         "To make training rare",
         "To avoid testing"
     ],
     "correct": 0,
     "explain": "Frequent refreshers maintain vigilance and counteract complacency."},

    {"question": "What is the role of leadership in security culture?",
     "options": [
         "Leaders model behavior, allocate resources, and prioritize security throughout the organization",
         "Leaders have no role",
         "Leaders should ignore security",
         "Leaders publish passwords"
     ],
     "correct": 0,
     "explain": "Leadership support makes security a priority and ensures effective programs."},

    {"question": "Why document security policies and procedures clearly?",
     "options": [
         "To provide actionable guidance that staff can follow consistently",
         "To keep rules secret",
         "To publish sensitive information",
         "To reduce training"
     ],
     "correct": 0,
     "explain": "Clear documentation helps consistent, auditable security practices."},

    {"question": "What is the value of role-based training?",
     "options": [
         "Provide tailored training for specific job functions and associated risks",
         "One-size-fits-all training is always best",
         "Role-based training exposes secrets",
         "Role training reduces awareness"
     ],
     "correct": 0,
     "explain": "Targeted training focuses on the threats and responsibilities relevant to each role."},

    {"question": "Why enforce strong physical security policies?",
     "options": [
         "To prevent unauthorized physical access that could enable data theft or system tampering",
         "To make offices inaccessible to employees",
         "To avoid locks",
         "To publish access credentials"
     ],
     "correct": 0,
     "explain": "Physical measures complement technical controls to secure assets."},

    {"question": "Why include privacy and security topics in onboarding?",
     "options": [
         "Early training sets expectations and reduces risky behavior from day one",
         "Onboarding should ignore security",
         "Onboarding must be delayed only",
         "Onboarding prevents updates"
     ],
     "correct": 0,
     "explain": "Initial training establishes secure practices and responsibilities from the start."},

    {"question": "Why track training completion and effectiveness?",
     "options": [
         "To ensure coverage and identify areas for improvement or targeted interventions",
         "To avoid measuring progress",
         "To publish incomplete results",
         "To reduce training quality"
     ],
     "correct": 0,
     "explain": "Metrics help refine programs and show impact on risk reduction."},

    {"question": "What is acceptable behavior with social media in a corporate context?",
     "options": [
         "Avoid sharing sensitive company information and follow guidelines for public posts",
         "Share everything publicly",
         "Post confidential updates regularly",
         "Ignore corporate guidelines"
     ],
     "correct": 0,
     "explain": "Protect company and personal privacy by following social media policies."},

    {"question": "Why encourage a reporting-first mindset when suspicious activity is found?",
     "options": [
         "Early reports enable quicker response and reduce harm rather than assigning blame",
         "To delay action",
         "To hide incidents",
         "To publicize incidents prematurely"
     ],
     "correct": 0,
     "explain": "Prompt reporting speeds containment and reduces damage."},

    {"question": "Why keep acceptable use policies accessible and updated?",
     "options": [
         "Accessible, current policies ensure users know expectations and changes are communicated",
         "To hide policies",
         "To change policies rarely",
         "To publish secrets publicly"
     ],
     "correct": 0,
     "explain": "Visibility and currency increase compliance and reduce misunderstandings."},

    {"question": "Why teach safe remote work habits?",
     "options": [
         "Remote environments introduce new risks like home network insecurity which users should mitigate",
         "Remote work is always insecure",
         "Remote work removes all risks",
         "Remote work is required without training"
     ],
     "correct": 0,
     "explain": "Guidance on VPNs, updates, and device security helps protect remote employees."},

    {"question": "Why include phishing simulations with educational follow-ups?",
     "options": [
         "Simulations with teaching help users learn from mistakes rather than just penalizing them",
         "Simulations should punish immediately",
         "Simulations are useless",
         "Simulations should be public"
     ],
     "correct": 0,
     "explain": "Learning from controlled simulations improves awareness and behavior."},

    {"question": "Why clearly define acceptable use for cloud storage?",
     "options": [
         "To prevent inappropriate sharing of sensitive data and enforce storage controls",
         "To allow unrestricted public sharing",
         "To disable encryption",
         "To post files publicly"
     ],
     "correct": 0,
     "explain": "Policies reduce accidental exposures and ensure compliance with retention and privacy rules."},

    {"question": "Why train staff about the risks of shadow IT?",
     "options": [
         "Shadow IT creates unmanaged services and data flows that increase risk; training and policies reduce its use",
         "Shadow IT always improves agility and security",
         "Shadow IT is required",
         "Shadow IT is irrelevant"
     ],
     "correct": 0,
     "explain": "Bring shadow IT into governance to control risk while enabling legitimate needs."},

    {"question": "Why promote a security-conscious culture?",
     "options": [
         "Culture influences daily decisions, encouraging safe behaviors and reporting that reduce overall risk",
         "Culture has no effect",
         "Culture should punish users",
         "Culture is irrelevant to security"
     ],
     "correct": 0,
     "explain": "A strong culture makes security part of normal operations, reducing human error."},

    {"question": "Why document and publish incident response contacts and processes?",
     "options": [
         "To ensure staff know how to report and who to contact quickly during an incident",
         "To hide contacts",
         "To publish passwords",
         "To avoid action"
     ],
     "correct": 0,
     "explain": "Clear contact information speeds coordinated response and reduces confusion."},

    {"question": "Why include privacy training for staff handling personal data?",
     "options": [
         "To ensure they understand legal obligations and practical measures to protect data",
         "To avoid compliance",
         "To publish personal data",
         "To ignore rules"
     ],
     "correct": 0,
     "explain": "Training reduces accidental breaches and supports lawful processing of personal data."}
]

# ------------------------------------------------------------
# Build master question bank (300 total) with category + difficulty tags
# ------------------------------------------------------------
_CATEGORY_LISTS = [
    ('Phishing',           phishing),
    ('Password Security',  passwords),
    ('Access Control',     access_control),
    ('Malware',            malware),
    ('Social Engineering', social_engineering),
    ('Email Security',     email_security),
    ('Network Safety',     internet_safety),
    ('Cryptography',       crypto),
    ('Secure Coding',      secure_software),
    ('Incident Response',  incident_response),
    ('Device Security',    device_security),
    ('Privacy & Ethics',   cyber_ethics),
    ('Security Awareness', security_awareness),
]

def _assign_difficulty(index: int, total: int) -> str:
    pct = index / max(total - 1, 1)
    if pct < 0.4:   return 'easy'
    if pct < 0.75:  return 'medium'
    return 'hard'

question_bank = []
for cat_name, cat_list in _CATEGORY_LISTS:
    for i, q in enumerate(cat_list):
        enriched = dict(q)
        enriched.setdefault('category',   cat_name)
        enriched.setdefault('difficulty', _assign_difficulty(i, len(cat_list)))
        question_bank.append(enriched)

# Trim to exactly 300 for consistency (keeps all 13 categories represented)
if len(question_bank) >= 300:
    question_bank = question_bank[:300]
else:
    i = 0
    while len(question_bank) < 300:
        question_bank.append(question_bank[i % len(question_bank)])
        i += 1

# ------------------------------------------------------------
# API: pick random 30 questions per session
# ------------------------------------------------------------
def get_random_questions(total=30, seed=None):
    """
    Return a random sample of 'total' questions from the bank.
    Optional seed for reproducibility in testing.
    """
    if seed is not None:
        rnd = random.Random(seed)
        return rnd.sample(question_bank, total)
    return random.sample(question_bank, total)

# Export 'quests' used by the game
quests = get_random_questions(30)