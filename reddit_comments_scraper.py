{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/wYSYfMvMwBx80fveGrdC"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from prawcore.exceptions import Forbidden"
      ],
      "metadata": {
        "id": "8BEIfvRC5Hrp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fKLg9t9BSJeW"
      },
      "outputs": [],
      "source": [
        "# Import Libraries\n",
        "import praw\n",
        "from praw.models import MoreComments\n",
        "\n",
        "def scrape_comments(url):\n",
        "  # Please change with your own client id, client secret, and user agent\n",
        "  # Initializing the client id, client secret, and user agent\n",
        "  reddit_read_only = praw.Reddit(client_id= '', #Enter your client id\n",
        "                     client_secret= '', #Enter your secret key\n",
        "                     user_agent= '', #Enter your user agent\n",
        "                     check_for_async = False)\n",
        "\n",
        "  # Creating a submission object\n",
        "  submission = reddit_read_only.submission(url=url)\n",
        "  return submission"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "posts_dict = {\"Title\": [], \"Post Text\": [],\n",
        "              \"ID\": [], \"Score\": [],\n",
        "              \"Total Comments\": [], \"Post URL\": []\n",
        "              }\n",
        "\n",
        "post_comments = scrape_comments(url)  #Please use the url of the reddit post\n",
        "#Print post id\n",
        "print(post_comments)\n",
        "\n",
        "all_comments = []\n",
        "for comment in post_comments.comments:\n",
        "    if type(comment) == MoreComments:\n",
        "        continue\n",
        "\n",
        "    all_comments.append(comment.body)\n",
        "\n",
        "# creating a dataframe\n",
        "comments_df = pd.DataFrame(all_comments, columns=['comment'])\n",
        "# saving the comments\n",
        "comments_df.to_excel(\"file_op_path/output.xlsx\", index=True)  #Enter the file output path"
      ],
      "metadata": {
        "id": "WclplDULf-Ce"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
