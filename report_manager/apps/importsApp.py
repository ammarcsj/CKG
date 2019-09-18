import config.ckg_config as ckg_config
from apps import basicApp
from apps import imports


class ImportsApp(basicApp.BasicApp):
    def __init__(self, title, subtitle, description, layout = [], logo = None, footer = None):
        self.pageType = "importsPage"
        basicApp.BasicApp.__init__(self, title, subtitle, description, self.pageType, layout, logo, footer)
        self.buildPage()

    def buildPage(self):
        self.add_basic_layout()
        stats_file = "../../data/imports/stats/stats.hdf"
        stats_df = imports.get_stats_data(stats_file, n=3)
        plots = []
        plots.append(imports.plot_total_number_imported(stats_df, 'Number of imported entities and relationships'))
        plots.append(imports.plot_total_numbers_per_date(stats_df, 'Imported entities vs relationships'))
        plots.append(imports.plot_databases_numbers_per_date(stats_df, 'Full imports: entities/relationships per database', key='full', dropdown=True, dropdown_options='dates'))
        plots.append(imports.plot_databases_numbers_per_date(stats_df, 'Partial imports: entities/relationships per database', key='partial', dropdown=True, dropdown_options='dates'))
        # plots.append(imports.plot_import_numbers_per_database(stats_df, 'Full imports: Breakdown entities/relationships', key='full', subplot_titles = ('Entities imported', 'Relationships imported', 'File size', 'File size'), colors=True, color1='entities', color2='relationships', dropdown=True, dropdown_options='databases'))
        plots.append(imports.plot_import_numbers_per_database(stats_df, 'Partial imports: Breakdown entities/relationships', key='partial', subplot_titles = ('Entities imported', 'Relationships imported', 'File size', 'File size'), colors=True, color1='entities', color2='relationships', dropdown=True, dropdown_options='databases'))
        self.extend_layout(plots)
