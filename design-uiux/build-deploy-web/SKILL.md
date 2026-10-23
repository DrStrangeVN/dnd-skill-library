---
name: build-deploy-web
description: Build, redesign, fix, verify, and deploy websites or web apps from concise user requests. Use when the user asks to create a website, landing page, web app, clone or adapt a web layout, improve an existing site, fix a web project, modernize UI/UX, or publish/deploy a site and return a public URL.
---

# AI Web Builder Pro

Turn a short brief into a complete, reviewable, deployable website with as little unnecessary back-and-forth as possible.

## Core outcome

Default workflow:

REQUEST → INFER REQUIREMENTS → DESIGN → IMPLEMENT → RUN → VERIFY → FIX → PRODUCTION BUILD → DEPLOY → VERIFY PUBLIC URL → REPORT

The task is not complete merely because source code exists. When deployment access is available and the user has asked for a live site, continue through deployment and return the working public URL.

## Interaction style

- Treat short prompts as sufficient when a reasonable implementation can be inferred safely.
- Do not ask the user to repeat information already present in the conversation, files, screenshots, references, repository, or connected services.
- Avoid unnecessary clarification when a reversible, professional default exists.
- Make sensible design and technical decisions autonomously.
- Ask only when a required decision cannot be inferred, credentials/authorization are needed, or an irreversible/high-impact action requires explicit approval.
- Keep progress updates concise and useful.
- Never claim deployment, tests, or verification succeeded unless they were actually performed.

## Default technical choices

When the user does not specify a stack, prefer:

- Next.js with App Router
- TypeScript
- Tailwind CSS
- shadcn/ui as the default component foundation when appropriate
- Lucide Icons
- Geist or Inter typography unless the brand suggests otherwise
- Modern responsive component architecture
- Vercel for deployment
- GitHub for repository hosting/version control when available

Use a simpler stack such as static HTML/CSS/JS or Vite when that is materially better for the request. Do not force Next.js when unnecessary.

## Premium 2026 UI/UX design language

Unless the user explicitly specifies another visual direction, use this as the default design language.

### Core visual direction

- Minimal, clean, lightweight, premium, calm, and highly usable.
- Draw inspiration from the interaction and visual discipline of Apple, Linear, Vercel, and polished modern SaaS products without copying them literally.
- Avoid a generic "AI-generated website" appearance.
- Prefer strong typography, spacing, hierarchy, and composition over decorative effects.
- Use generous whitespace and clear visual breathing room.
- Use neutral or brand-led palettes with one primary accent color unless the brief calls for more.
- Prefer subtle borders, tonal surfaces, and restrained elevation over heavy drop shadows.
- Use soft rounded corners, generally around 10–16px, while adapting to brand personality.
- Keep each section focused. Prefer one or two dominant visual ideas instead of many competing elements.
- Use crisp iconography, consistent spacing tokens, and a coherent grid.
- Support light/dark modes when appropriate, but do not add them mechanically if they do not benefit the product.

### Avoid by default

- Excessive gradients.
- Neon glows everywhere.
- Full-page glassmorphism.
- Large amounts of blur or translucency that reduce readability.
- Decorative 3D that increases weight without adding value.
- Constant looping animation.
- Oversized pill buttons everywhere.
- Random floating cards or blobs with no information purpose.
- Excessively large hero text that harms usability.
- Too many colors, fonts, border radii, or shadow styles.
- Visual effects used only to make a page look "AI-ish" or trendy.

### Component preference order

Before creating a custom component from scratch, check whether the project already has a suitable component. If not, prefer these design sources conceptually in this order when compatible with the project:

1. shadcn/ui — base primitives and common product UI.
2. Origin UI — polished minimal SaaS/dashboard components.
3. Motion Primitives — subtle motion and micro-interactions.
4. Magic UI — selected hero/marketing accents only.
5. React Bits — selected animated/background/text effects only.

Do not blindly copy demo styling. Adapt every borrowed component into one consistent project-specific design system.

### Motion rules

- Motion must be subtle, purposeful, and functional.
- Typical duration: approximately 150–300ms.
- Prefer fade, slide, scale, accordion, layout, and state transitions.
- Use motion to clarify hierarchy, state, navigation, or feedback.
- Avoid continuous animation unless it communicates meaningful status or the user explicitly requests it.
- Respect reduced-motion preferences.

### Layout rules

- Mobile-first responsive layout.
- Use clear max-width containers and predictable spacing scales.
- Maintain strong vertical rhythm.
- Use Bento Grid only when it improves information hierarchy or storytelling; never use it automatically just because it is fashionable.
- Keep navigation simple and obvious.
- Avoid overcrowding cards, dashboards, and hero sections.
- On mobile, prioritize the primary user task and remove decorative complexity before shrinking everything.

### Typography rules

- Typography is a primary design tool.
- Prefer Geist, Inter, or an appropriate high-quality brand font.
- Use a restrained type scale with clear heading/body hierarchy.
- Keep body copy readable with comfortable line-height and line length.
- Avoid using too many font weights.
- Use uppercase sparingly.

### Performance rules

- Visual polish must not materially harm performance.
- Keep dependencies minimal.
- Avoid unnecessary client-side JavaScript.
- Prefer CSS for simple visual effects and transitions.
- Lazy-load heavy visual elements when appropriate.
- Optimize images and fonts.
- Avoid adding animation/component libraries when native CSS or existing dependencies are sufficient.
- Preserve excellent Core Web Vitals/Lighthouse performance whenever practical.

## Context-specific visual presets

Infer the most appropriate preset from the user's product instead of applying one style to everything.

### Product / dashboard / internal tool

Default direction:
- Linear/Vercel-inspired product UI.
- shadcn/ui + Origin UI style discipline.
- Dense enough for productivity, but never cluttered.
- Strong states, tables, filters, forms, empty states, keyboard usability, and responsive behavior.
- Minimal decorative motion.

### Sports / entertainment brand

Default direction:
- Editorial minimal with strong photography, bold typography, and controlled brand accents.
- Bento layout may be used selectively for stats, highlights, fixtures, media, or stories.
- Use energetic motion only at meaningful moments.
- Avoid turning the entire interface into a gaming/neon aesthetic unless requested.

### Corporate / agency / event company

Default direction:
- Premium corporate minimal.
- Strong black/white or neutral foundation with brand accent.
- Apple/Vercel-like spacing discipline.
- Subtle glass or translucent surfaces only in selected areas when it supports the brand.
- High-quality imagery and refined typography over visual gimmicks.

### Ecommerce

Default direction:
- Editorial commerce.
- Large, high-quality product photography.
- Minimal navigation and clean product grids/cards.
- Clear price, variant, cart, and checkout hierarchy.
- Very restrained animation so shopping remains fast.

### Operational tools / scoreboard / control panels

Default direction:
- Utility-first UI.
- Large, obvious controls.
- High contrast and strong state visibility.
- Zero unnecessary animation.
- Fast interaction and error prevention take priority over decorative style.

### Landing pages / marketing sites

Default direction:
- Strong hero, concise value proposition, clear CTA, visual proof, benefits, trust, and conversion flow.
- Use Magic UI, React Bits, or richer motion only for selected focal moments.
- Keep the majority of the page clean and static so the accent moments feel intentional.

## Design quality ratio

As a default mental model, aim for roughly:

- 80% clean component/system foundation (shadcn/Origin-like discipline)
- 15% typography, spacing, hierarchy, imagery, and brand expression
- 5% motion or visual effects

This is not a mathematical requirement. The principle is: premium design should come primarily from composition and consistency, not from effects.

## Design defaults

Unless the user specifies otherwise:

- Mobile-first responsive layout
- Strong hierarchy and clear CTA structure
- Professional spacing and typography
- Accessible contrast and keyboard-friendly interaction
- Lightweight motion only when it improves the experience
- Reusable components and consistent visual tokens
- Sensible empty, loading, error, and success states where relevant
- Avoid generic-looking template output; tailor visual language to the brand, industry, audience, and brief
- Maintain a consistent visual system across every page rather than designing each section independently

If brand assets, screenshots, references, copy, or files are supplied, inspect and use them before inventing replacements. Explicit user references override the default 2026 visual language when they conflict.

## Design decision process

Before implementation, infer:

1. Product type and primary user task.
2. Audience and brand personality.
3. Information density required.
4. Most appropriate context-specific preset above.
5. Required visual hierarchy and primary CTA/action.
6. Whether motion meaningfully helps.
7. Whether a component already exists before creating a new dependency.

For redesign tasks, preserve strong existing brand identity while improving hierarchy, spacing, typography, component consistency, responsive behavior, accessibility, and performance.

## New website workflow

1. Infer the site's purpose, target audience, likely conversion goal, key sections, and content needs from the brief.
2. Choose an appropriate architecture and information hierarchy.
3. Select the best context-specific visual preset and adapt it to the brand.
4. Build the full site, not placeholder wireframes, unless the user explicitly asks for a prototype.
5. Include polished placeholder copy only when real copy is unavailable, and make it easy to replace.
6. Implement responsive behavior for common desktop, tablet, and mobile widths.
7. Run the project locally.
8. Check console/build/runtime errors and fix them.
9. Run a production build and resolve failures.
10. Verify key navigation, CTAs, forms, and user flows where practical.
11. Deploy when requested and access is available.
12. Open the deployed URL and verify that the public site loads correctly before reporting completion.

## Existing project workflow

When the user provides or references an existing project/repository:

- Inspect the current project before changing architecture.
- Preserve working conventions unless there is a clear reason to change them.
- Reuse the existing deployment/project when possible instead of creating duplicates.
- Respect the project's existing design system unless the user asks for a redesign.
- When redesigning, migrate toward the premium 2026 principles without unnecessarily rewriting stable logic.
- Make requested changes, then run tests/build and verify affected flows.
- If the project is already deployed, update the existing deployment when authorized rather than silently creating a separate site.

## Reference-to-web workflow

When given a screenshot, design, URL, PDF, slide, document, or image as reference:

- Extract the layout, hierarchy, components, brand cues, and copy structure.
- Recreate the overall experience without copying protected source code or hidden implementation details.
- If asked to closely reproduce a visual reference, match spacing, proportions, typography feel, and interaction patterns as closely as practical while using independently written code.
- Adapt the result responsively instead of treating the reference as a single fixed-size image.
- If the reference is visually dated, preserve the recognizable brand/content structure while modernizing execution unless the user asks for an exact period look.

## Deployment policy

When the user asks to publish, deploy, host, or give them a live link:

1. Prefer Vercel for Next.js/React projects unless another host is clearly better or the user specifies one.
2. Use available Vercel deployment capabilities or CLI/tools in the environment.
3. Use GitHub when useful for persistent source/version control and when access is available.
4. Do not expose secrets, tokens, private environment variables, or credentials.
5. If environment variables are required, use the platform's secure environment configuration rather than hard-coding secrets.
6. After deployment, verify the public URL actually resolves and the page renders.
7. Return the exact public URL plus a concise summary of what was deployed.
8. If deployment is blocked by missing authorization, finish everything that can be completed first, then ask only for the specific required authorization step.

## Vercel/GitHub behavior

- Prefer linking an existing GitHub repository to Vercel when one already exists.
- For a new project, create a clean repository only when repository access is available and the user wants or benefits from persistent source control.
- Do not create duplicate Vercel projects or repositories without a reason.
- For subsequent requests such as “fix web hôm qua”, “update bản mới”, or “deploy lại”, identify and continue with the existing project whenever the conversation or connected services make that unambiguous.

## Verification checklist

Before calling the result complete, perform the applicable checks:

- Install succeeds
- Development server starts
- Production build succeeds
- No obvious runtime errors
- Main pages render
- Primary navigation works
- Main CTA works
- Forms have basic validation and useful feedback
- Mobile layout is usable
- Images/assets load
- Visual hierarchy is coherent on desktop and mobile
- Interactive states (hover/focus/active/disabled) are intentional
- Motion does not impair usability or reduced-motion accessibility
- No obvious generic AI-template artifacts or gratuitous effects
- Public deployment loads successfully

If one of these cannot be checked, state that limitation specifically instead of implying it was verified.

## SEO and production basics

For public-facing sites, add reasonable defaults when appropriate:

- Meaningful page title and meta description
- Open Graph metadata
- Favicon/app icon when practical
- Semantic headings and landmarks
- Image alt text
- Basic performance-conscious asset handling
- robots/sitemap only when useful for the project

Do not overengineer analytics, auth, databases, or CMS features unless the brief needs them.

## Short commands and intent aliases

Interpret these as workflow aliases even if the user does not literally use slash commands:

- `/buildweb` — create a complete site from a brief
- `/landingpage` — create a focused conversion landing page
- `/website` — create or continue a website
- `/webapp` — create an interactive web application
- `/redesign` — modernize or restyle an existing website using the premium 2026 design language unless another style is specified
- `/ui2026` — apply the premium minimal 2026 design language to the current site or feature
- `/fixweb` — diagnose and repair an existing web project
- `/cloneweb` — recreate/adapt a reference layout with independently written code
- `/deploy` — build, deploy, verify, and return the live URL

Also understand natural-language requests such as:

- “Thiết kế theo UI/UX 2026.”
- “Làm giao diện kiểu Steven UI 2026.”
- “Làm sạch, nhẹ, premium, tối giản.”
- “Làm kiểu Vercel/Linear nhưng theo brand của tôi.”

Treat these as requests to apply the design language defined above, not as requests to literally copy another product.

## Completion format

At the end of a successful build/deploy task, provide a compact handoff containing:

- Public URL, if deployed
- Source/repository location, if created or updated
- What was built or changed
- Which visual direction/preset was used when relevant
- Verification performed
- Any remaining item that genuinely requires the user's input

Do not bury the public URL when the user primarily asked for a live website.
