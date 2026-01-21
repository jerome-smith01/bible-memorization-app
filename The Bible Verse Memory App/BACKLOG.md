# Bible Memorization Assistant - Development Backlog

Last Updated: January 20, 2026

---

## 🚀 Priority 1: Production Deployment (Critical)

These must be done before going live to Netlify.

### PD1: GitHub Repository Setup
- [ ] Create GitHub repository
- [ ] Push all code to GitHub (keeping `.env` private with `.gitignore`)
- [ ] Set up GitHub Actions for CI/CD (optional but recommended)
- [ ] Document GitHub setup in deployment guide

### PD2: Backend Deployment to Render
- [ ] Create Render account
- [ ] Connect GitHub repository to Render
- [ ] Deploy Flask backend
- [ ] Test all endpoints on Render URL
- [ ] Document Render deployment steps

### PD3: Frontend Deployment to Netlify
- [ ] Create Netlify account
- [ ] Update `index.html` API_BASE_URL to Render backend URL
- [ ] Deploy to Netlify from GitHub or manual upload
- [ ] Test all features on live Netlify URL
- [ ] Set up custom domain (optional)

### PD4: Environment Variables Configuration
- [ ] Create `.env` file with Resend API key (if using email)
- [ ] Create `.env` file with Google OAuth credentials (if using Google Tasks)
- [ ] Document in `.env.example` which variables are required vs optional
- [ ] Add environment setup instructions to DEPLOYMENT_GUIDE.md

---

## 🔧 Priority 2: Bug Fixes & Stability (High)

These improve reliability and user experience.

### BF1: Schedule Download Bug ✅ FIXED (Jan 20, 2026)
- [x] Fixed missing `await` on `response.json()` in JavaScript
- [x] Fixed validation to allow optional verse end
- [x] Default verse end to verse start if not provided
- **Status**: Download now works correctly

### BF2: Error Handling Improvements
- [ ] Add try-catch around file operations in Python
- [ ] Better error messages for invalid book names
- [ ] Validate chapter/verse numbers exist before fetching
- [ ] Return user-friendly error messages instead of raw exceptions
- [ ] Log errors to file (not just console)

### BF3: Input Validation
- [ ] Sanitize user input (book names, emails)
- [ ] Validate email format before sending
- [ ] Check verse numbers are positive integers
- [ ] Verify chapter numbers are within valid range for each book
- [ ] Provide inline validation feedback in UI

### BF4: Calendar File Handling
- [ ] Ensure .ics files are valid RFC 5545 format
- [ ] Test import into Google Calendar, Apple Calendar, Outlook
- [ ] Handle special characters in file names
- [ ] Add file size limits to prevent memory issues
- [ ] Clean up old .ics files from data/ folder (optional archival)

---

## ✨ Priority 3: Feature Enhancements (Medium)

These add new capabilities but aren't critical.

### FE1: Email Integration
- [ ] Complete Resend API integration
- [ ] Send .ics attachment via email
- [ ] Add email templates (HTML formatted emails)
- [ ] Test email delivery
- [ ] Handle email bounces gracefully
- [ ] Add unsubscribe/preference link to emails

### FE2: Google Tasks Integration
- [ ] Implement Google OAuth 2.0 flow
- [ ] Add "Create in Google Tasks" output method
- [ ] Create "Daily Bread" task list in user's Google Tasks
- [ ] Daily recurring tasks with memory aid description
- [ ] Sync with user's calendar if desired
- [ ] Handle OAuth token refresh

### FE3: User Authentication
- [ ] Add user login/signup system
- [ ] Persist user data per account
- [ ] Allow multiple users on same app instance
- [ ] Implement JWT or session-based auth
- [ ] Add logout functionality
- [ ] Secure password storage (bcrypt hashing)

### FE4: UI/UX Improvements
- [ ] Add keyboard shortcuts (Enter to submit forms)
- [ ] Improve mobile responsiveness (test on various devices)
- [ ] Add dark mode toggle
- [ ] Show verse reference tooltip on memory aid
- [ ] Add verse search functionality (search by content, not just reference)
- [ ] Remember last used book/chapter preference
- [ ] Add favorites/bookmarked verses
- [ ] Show reading plan suggestions

### FE5: Advanced Scheduling
- [ ] Allow custom start dates (not just today)
- [ ] Adjustable reminder times for each event
- [ ] Pause/resume memorization schedule
- [ ] Change progression interval mid-schedule
- [ ] Mark verses as "completed"
- [ ] Track memorization progress
- [ ] Generate completion certificates

### FE6: Content Management
- [ ] Support multiple Bible versions (not just Recovery Version)
- [ ] Add Bible version selector in preferences
- [ ] Support for different languages
- [ ] Add commentary/cross-references for each verse
- [ ] Export schedule as PDF instead of just .ics
- [ ] Create printable memory cards

---

## 🧪 Priority 4: Testing & Documentation (Medium)

These ensure quality and maintainability.

### TD1: Automated Testing
- [ ] Write unit tests for Bible fetcher
- [ ] Write tests for verse initializer formatting
- [ ] Write tests for calendar generator
- [ ] Write tests for schedule logic
- [ ] Add pytest framework
- [ ] Set up GitHub Actions to run tests on push
- [ ] Achieve 80%+ code coverage

### TD2: API Documentation
- [ ] Create OpenAPI/Swagger documentation
- [ ] Add request/response examples for each endpoint
- [ ] Document error codes and messages
- [ ] Add authentication section (when implemented)
- [ ] Create Postman collection for testing

### TD3: User Documentation
- [ ] Create tutorial videos (YouTube)
- [ ] Create FAQ page
- [ ] Add in-app tooltips and help text
- [ ] Create admin documentation
- [ ] Document database schema (if upgraded from JSON)
- [ ] Create troubleshooting guide for common issues

### TD4: Code Documentation
- [ ] Add docstrings to all Python functions
- [ ] Add JSDoc comments to JavaScript functions
- [ ] Create architecture diagram
- [ ] Document data flow and dependencies
- [ ] Add comments for complex algorithms
- [ ] Create developer setup guide

---

## 📊 Priority 5: Performance & Scalability (Low)

These improve efficiency but aren't blocking.

### PS1: Caching
- [ ] Implement Redis caching for Bible verses
- [ ] Cache user preferences
- [ ] Add browser caching headers for static files
- [ ] Implement service worker for offline support
- [ ] Cache calendar generation results

### PS2: Database Migration
- [ ] Migrate from JSON files to PostgreSQL
- [ ] Add database connection pooling
- [ ] Implement database migrations with Alembic
- [ ] Add database backups
- [ ] Optimize queries with indexes

### PS3: Performance Optimization
- [ ] Minify CSS/JavaScript in production
- [ ] Compress images and assets
- [ ] Implement lazy loading for verses
- [ ] Add pagination for large lists
- [ ] Profile and optimize slow endpoints
- [ ] Add CDN for static files

### PS4: Rate Limiting & Security
- [ ] Add rate limiting to API endpoints
- [ ] Implement CORS properly (not * for all)
- [ ] Add request validation middleware
- [ ] Implement API key authentication (if public API)
- [ ] Add HTTPS enforcement
- [ ] Prevent SQL injection (even with JSON, good practice)

---

## 🔐 Priority 6: Security & Compliance (Medium)

These ensure the app is secure and compliant.

### SC1: Security Hardening
- [ ] HTTPS/SSL enforcement
- [ ] Security headers (CSP, X-Frame-Options, etc.)
- [ ] CORS configuration review
- [ ] Input sanitization across all endpoints
- [ ] Dependency vulnerability scanning
- [ ] Regular security audits

### SC2: Copyright & Licensing
- [ ] Verify Recovery Version Bible copyright compliance
- [ ] Add proper attribution on downloads
- [ ] Create terms of service
- [ ] Add privacy policy
- [ ] Document Bible content licensing in README
- [ ] Add license headers to source files

### SC3: Data Privacy
- [ ] GDPR compliance (if EU users)
- [ ] Data retention policies
- [ ] User data export functionality
- [ ] Right to be forgotten implementation
- [ ] Privacy impact assessment
- [ ] Data encryption at rest

---

## 📱 Priority 7: Native & Mobile (Nice to Have)

These extend the app to other platforms.

### NM1: Progressive Web App (PWA)
- [ ] Add service worker for offline support
- [ ] Create app manifest for install prompt
- [ ] Implement app icons and splash screens
- [ ] Add push notifications
- [ ] Allow installation on home screen

### NM2: Mobile App (Electron/React Native)
- [ ] Create Electron wrapper for desktop
- [ ] Create React Native app for iOS/Android
- [ ] Native push notifications
- [ ] Camera access for verses (optional OCR)
- [ ] Offline storage with sync

### NM3: Browser Extensions
- [ ] Chrome extension for quick verse lookup
- [ ] Firefox add-on
- [ ] Right-click context menu integration
- [ ] Highlight verses on web pages

---

## 🎯 Quick Reference: Status Summary

| Category | Total | Done | In Progress | Not Started |
|----------|-------|------|-------------|-------------|
| Deployment | 4 | 0 | 0 | 4 |
| Bug Fixes | 4 | 1 | 0 | 3 |
| Features | 6 | 0 | 0 | 6 |
| Testing | 4 | 0 | 0 | 4 |
| Performance | 4 | 0 | 0 | 4 |
| Security | 3 | 0 | 0 | 3 |
| Mobile | 3 | 0 | 0 | 3 |
| **TOTAL** | **28** | **1** | **0** | **27** |

---

## 🎬 Getting Started - Next Steps

### This Week
1. ✅ Fix schedule download bug → **DONE**
2. Test all features thoroughly on `http://127.0.0.1:5000`
3. Create GitHub repository
4. Push code to GitHub

### Next Week
1. Deploy backend to Render
2. Deploy frontend to Netlify  
3. Test live on Netlify URL
4. Share with friends/family for feedback

### This Month
1. Fix any bugs from live testing
2. Basic error handling improvements
3. Email integration (if needed)
4. Update documentation based on user feedback

---

## 💡 Feature Ideas for Future

**User-Suggested Features** (collected from users):
- [ ] Email reminders at specific time
- [ ] Group sharing of schedules
- [ ] Leaderboard/achievements
- [ ] Community verse sharing
- [ ] Audio pronunciation of verses
- [ ] Spaced repetition algorithm
- [ ] Quiz/test functionality
- [ ] Progress tracker dashboard

**Potential Partnerships:**
- [ ] Integration with Bible study apps (YouVersion, etc.)
- [ ] Church management systems integration
- [ ] Small groups coordination
- [ ] Sunday school curriculum alignment

---

## 📝 Notes

### Known Limitations
1. **Bible Content**: Only Recovery Version available (can be extended)
2. **Storage**: JSON files only (should migrate to database for scale)
3. **Auth**: No user login system yet (needed for multi-user)
4. **Email**: Optional (requires API key configuration)
5. **Google Tasks**: Not implemented (requires OAuth setup)

### Technical Debt
1. Replace print statements with proper logging
2. Add comprehensive error handling
3. Refactor long functions into smaller units
4. Add type hints to Python code
5. Move hardcoded values to config file

### Code Improvements Needed
1. Add input validation middleware
2. Implement caching for Bible verses
3. Optimize database queries (when migrating from JSON)
4. Add request/response logging
5. Implement API versioning (/api/v1/...)

---

## 🔄 Maintenance Tasks (Recurring)

- [ ] Weekly: Check logs for errors
- [ ] Weekly: Test main features
- [ ] Monthly: Check for dependency updates
- [ ] Monthly: Review performance metrics
- [ ] Quarterly: Security audit
- [ ] Quarterly: Code review and refactoring

---

**Last Updated**: January 20, 2026  
**Created By**: Copilot  
**Version**: 1.0
