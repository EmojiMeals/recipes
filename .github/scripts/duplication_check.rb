require 'set'
require 'json'

recipes = JSON.parse(File.read('recipes.json'))
recipes_set = Set.new()
recipes.keys.each_with_index do |ingredients, index|
  recipes_set.add(Set.new(ingredients.chars).hash)
  raise "Duplicate ingredients found: #{ingredients.chars.join(" + ")}" if recipes_set.length < index + 1
end