---
name: umms-lunch-menu
description: Check the Upper Merion Middle School lunch menu for today or a specific date.
disable-model-invocation: true
---

Check the Upper Merion Middle School lunch menu for the requested date. If no date is provided via $ARGUMENTS, use today's date.

## Steps

1. **Fetch the menu page** at `https://www.umasd.org/departments/food-services/middle-school-menus` using WebFetch to find the PDF link for the correct month.

2. **Download the PDF** using `curl` to `/tmp/um_lunch_menu_<month>.pdf`. The PDFs are hosted on `resources.finalsite.net`.

3. **Convert to images** using `pdftoppm -png -r 200` to generate PNG files from the PDF pages.

4. **Read the PNG images** to visually interpret the calendar-style menu grid.

5. **Find the correct date** on the menu and extract all items for that day, organized by station:
   - Pizza Station
   - Fresh Cold Deli Station
   - Grille Station
   - Special of the Day
   - Sides

6. **Present the menu** in a clean, readable format with all options listed.

## Notes

- The menu is a Canva-designed visual layout (not text-extractable), so PDF-to-image conversion is required.
- `poppler` must be installed (`brew install poppler`) for `pdftoppm`.
- The school follows a Monday-Friday schedule. If the requested date falls on a weekend or holiday, note that.
- Menus are subject to change per the school's disclaimer.
