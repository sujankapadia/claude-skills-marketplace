---
name: umms-food-menu
description: Check the Upper Merion Middle School breakfast and lunch menus for today or a specific date.
disable-model-invocation: true
argument-hint: "[date]"
---

Check the Upper Merion Middle School breakfast and lunch menus for the requested date. If no date is provided via $ARGUMENTS, use today's date.

## Steps

1. **Fetch the menu page** at `https://www.umasd.org/departments/food-services/middle-school-menus` using WebFetch to find the PDF links for the correct month. There are separate PDFs for breakfast and lunch.

2. **Download both PDFs** using `curl` to `/tmp/um_lunch_menu_<month>.pdf` and `/tmp/um_breakfast_menu_<month>.pdf`. The PDFs are hosted on `resources.finalsite.net`.

3. **Convert to images** using `pdftoppm -png -r 200` to generate PNG files from each PDF's pages.

4. **Read the PNG images** to visually interpret the calendar-style menu grids.

5. **Find the correct date** on both menus and extract all items for that day.

   For **breakfast**, items are typically organized as:
   - Main Entrees (select one)
   - Sides

   For **lunch**, items are typically organized as:
   - Pizza Station
   - Fresh Cold Deli Station
   - Grille Station
   - Special of the Day
   - Sides

6. **Present both menus** in a clean, readable format with breakfast first, then lunch.

## Notes

- The menus are Canva-designed visual layouts (not text-extractable), so PDF-to-image conversion is required.
- `poppler` must be installed (`brew install poppler`) for `pdftoppm`.
- The school follows a Monday-Friday schedule. If the requested date falls on a weekend or holiday, note that.
- Breakfast is available to all students at no cost.
- Menus are subject to change per the school's disclaimer.
