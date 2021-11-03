# 🔐 Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.

### Authorization

Authorization is a process of determining if the user is allowed to access a resource.

#### RBAC (Role based access control)

The most common method. Define allowed roles for a resource and then check if a user has the allowed role in order to access a resource. Good example is `USER` and `ADMIN` roles. You want to restrict some things for users and let admins access it.

#### PBAC (Permission based access control)

Sometimes RBAC is not enough. Some of the operations should be allowed only by the owner of the resource. For example user's comment - only the author of the comment should be able to delete it. That's why you might want to use PBAC, as it is more flexible.

For RBAC protection you can use the `RBAC` component by passing allowed roles to it. On the other hand if you need more strict protection, you can pass policies check to it.
