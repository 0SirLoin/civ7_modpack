# HowTo

- Download mods.zip ("https://github.com/0SirLoin/civ7_modpack/releases/download/v3/SirLoinsModpack.zip")
- Unpack the zip file
- Copy all files to %USERPROFILE%/AppData/Local/Firaxis Games/Sid Meier's Civilization VII/Mods
- ???
- Profit

# Changelog
## Sir Loin's ModPack v3
- bugfix: unique quarter placement fixed with removing ui/building-placement from KayleeR's Misc UI Modifications
- added: "https://forums.civfanatics.com/resources/completed-production.32026/"
  - Displays the last completed item on the city production screen on the turn it is completed
- added: "https://forums.civfanatics.com/resources/tbqs-resource-allocation-improvements.32025/"
  - Remove all assigned resources from all settlements with the click of a button
  - Autosort Settlements
    - Capital first, then cities, finally towns
    - Within a category (city or town) sort by
      - Larger resource capacity
      - Then alphabetically by localized city name
      - Razed settlements always come last in their group
  - Keep all resource lists sorted too
  - Middle click an assigned resource to immediately unassign it from a settlement, if possible
  - Add a Show Cities toggle next to Show Towns
  - Remove settlement type ('Capital', 'City', and 'Town') appended to name. There's already an icon
- added: "https://forums.civfanatics.com/resources/leonardfactorys-policy-yield-previews.32012/"
  - Adds estimated yield previews for Social Policy (and Crisis Policy) cards on the Government screen, allowing you to better evaluate the current impact of each policy card.
- added: "https://forums.civfanatics.com/resources/resource-improvements.32009/"
  - Adds a filter to the Trade Panel that shows up when you click a trader, letting you sort the list by a certain resource or yield type you want (say you want Fish for your factory in the Modern era, you could sort for the trade routes with the most Fish).
  - Also adds a toggle so that untradeable cities are still included in the initial sort, meaning you dont have to scroll all way the down to see the best ones if you needed to Improve Trade Relations.
- added: "https://forums.civfanatics.com/resources/border-toggles.32008/"
  - This adds a toggle to show city borders, showing you which tile belong to which city if two cities overlap. It also adds a toggle to hide all borders, for screenshots or any other purpose. You'll find both toggles along the lenses just above the mini map.
- added: "https://forums.civfanatics.com/resources/sibr3s-transparent-appeal.32000/"
  - This very simple mod makes some adjustments to the colour and transparency values of the 'appeal layer' of the Settler Lens. The original layer, in my opinion, made it difficult to see the terrain underneath on unrevealed/non-highlighted map tiles.
- added: "https://forums.civfanatics.com/resources/chrispressos-debug-console-cdc.31995/
  - In order to bring it up hit Ctrl + D. Same command to hide/remove it.
- update: Better Main Menu to v1.1
  - Updated for game version 1.1.0
  - Rearranged additional content menu and added dividers (thanks for @Seek for the suggestion)
- update: bz-map-trix to v1.5.0
  - more visibility for damaged tiles
  - added current and maximum specialists to district tooltips
  - Italian translation by leonardfactory
  - Korean translation by Hotsolidinfill
  - Russian translation by Webrok (thanks!)
  - many small improvements to layout
  - more city center stats: religion and fresh water
  - highlighting for roads, obstacles, and hazardous effects
- update: Civ7EnhancedTownFocusInfo to v1.1.8
  - Added Simplified Chinese language support (thanks to thendye!)
  - Updated documentation
  - Minor code improvements
- update: F1rstDan's Cool UI to v1.5.0
  - "City Yield Panel"
      - Added display of city population information.
      - Added display of city connectivity information.
      - (Fewer words, bigger changes. A lot of work was done behind the scenes.)
   - Refactored and separated the Tooltip interface
      - Brand-new design, more visually appealing.
      - Details are now displayed in a table for better readability.
      - Tooltip no longer disappears when the mouse moves slightly.
      - Different resources have different text colors.
   - Resource income panel optimization
      - Different resources have different text colors.
      - Removed unnecessary ".0" in numbers.
- update: Immersive Diplomacy Screen to v1.3
  - Updated for game version 1.1.0
- update: Prismatic to v1.1.0
  - Updated for 1.1.0 patch
- update: Sukritacts to v.0.143
  - Fixed issue where overbuilding was not displaying the correct amounts for Full Tile Buildings
  - Added specialist count to plot tooltip
  - Updated Spanish and Russian Translations
  - Added German and a partial Traditional Chinese translation.
  - Added/Updated multiple translations
  - Added icons for common unlocks (settlement relic, relics, specialist limit) on the civics/techs panels/trees.
  - The Founder now uses the same lens as the Settler, so it will no longer toggle off yields/resources.
- update: KayleeR's Misc UI Modifications to 1.13
  - Update for compatibility with base game 1.1.0 patch
  - Improve discovery lens to update in fog of war (as this is consistent with how the tile constructible is visible)
- remove: Show Policy Yields

## Sir Loin's ModPack v2
- manually removed mod conflict files

## Sir Loin's ModPack v1
- initial release

# Modifications
- Settlement-View Alternative UI
  - remove interface-modes/support-city-decoration.js
- KayleeR's Misc UI Modifications
  - remove ui/lenses/layer/discovery-layer.js
  - remove ui/lenses/layer/building-placement-layer.js
  - remove ui/building-placement
  - remove ui/interface-modes/interface-mode-place-building.js
  - remove ui/resource-allocation/model-resource-allocation.js
  - remove ui/resource-allocation/screen-resource-allocation.js
  - remove ui/resource-allocation/screen-resource-allocation.css
- danield1909-lens-pack
  - remove ui/place-building/
  - remove ui/trade-route-chooser/trade-route-chooser.js
- Sukritact's Simple UI Adjustments
  - remove ui/utilities/utilities-textprovider.js
- Resource-Screen-Improvements
  - remove ui/resource-allocation/screen-resource-allocation.js
