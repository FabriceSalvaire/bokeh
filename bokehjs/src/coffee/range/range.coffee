_ = require "underscore"
HasProperties = require "../common/has_properties"

class Range extends HasProperties
  type: 'Range'

  defaults: ->
    return _.extend {}, super(), {
      callback: null
    }

  reset: () ->

module.exports =
  Model: Range