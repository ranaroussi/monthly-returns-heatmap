#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Monthly Returns Heatmap
# https://github.com/ranaroussi/monthly-returns-heatmap
#
# Copyright 2017 Ran Aroussi
#
# Licensed under the GNU Lesser General Public License, v3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__version__ = "0.0.2"
__author__ = "Ran Aroussi"
__all__ = ['get', 'plot']

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.base import PandasObject


def get(returns):

    # resample to business month
    returns = returns.resample('BMS').sum()

    # get close / first column if given DataFrame
    if isinstance(returns, pd.DataFrame):
        returns.columns = map(str.lower, returns.columns)
        if len(returns.columns) > 1 and 'close' in returns.columns:
            returns = returns['close']
        else:
            returns = returns[returns.columns[0]]

    # get returnsframe
    returns = pd.DataFrame(data={'Returns': returns})
    returns['Year'] = returns.index.strftime('%Y')
    returns['Month'] = returns.index.strftime('%b')

    # make pivot table
    returns = returns.pivot('Year', 'Month', 'Returns').fillna(0)

    # order columns by month
    returns = returns[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]

    return returns


def plot(returns,
         title="Monthly Returns (%)",
         title_color="black",
         title_size=12,
         annot_size=10,
         figsize=None,
         cmap='RdYlGn',
         cbar=True,
         square=False):

    returns = get(returns)
    returns *= 100

    if figsize is None:
        size = list(plt.gcf().get_size_inches())
        figsize = (size[0], size[0] // 2)
        plt.close()

    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.heatmap(returns, ax=ax, annot=True,
                     annot_kws={"size": annot_size}, fmt="0.2f", linewidths=0.5,
                     square=square, cbar=cbar, cmap=cmap)
    ax.set_title(title, fontsize=title_size, color=title_color, fontweight="bold")

    fig.subplots_adjust(hspace=0)
    plt.yticks(rotation=0)
    plt.show()
    plt.close()


PandasObject.get_returns_heatmap = get
PandasObject.plot_returns_heatmap = plot
