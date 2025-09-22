# Soft Launch Checklist

## Essential Pre-Launch
- [ ] No secrets/keys in code (check .env, configs)
- [ ] LICENSE file exists (MIT)
- [ ] Core functionality works (wake, wind-down, sign-off)
- [ ] README is clear and under 250 lines
- [ ] Install script works on clean system

## Quick Security Check
```bash
# Run these before going public
grep -r "api[_-]key\|secret\|token\|password" --include="*.py" --include="*.md" .
python3 scripts/security_check.py
```

## Minimal Launch
1. Make repo public
2. Tag v1.0.0-beta.1
3. Share with 3-5 developers for feedback
4. Iterate based on real usage

## Success =
- Someone can install and use it without asking questions
- No security issues reported
- Basic functionality works as advertised

Keep it simple. Ship it. Learn. Iterate.