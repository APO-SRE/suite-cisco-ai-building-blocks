from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activities_collection import ActivitiesCollection
from ...models.list_activities_response_400 import ListActivitiesResponse400
from ...models.list_activities_response_401 import ListActivitiesResponse401
from ...models.list_activities_response_403 import ListActivitiesResponse403
from ...models.list_activities_response_404 import ListActivitiesResponse404
from ...models.list_activities_response_500 import ListActivitiesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    event_type: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["event_type"] = event_type

    params["ids"] = ids

    params["created_after"] = created_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/activities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListActivitiesResponse400,
        ListActivitiesResponse401,
        ListActivitiesResponse403,
        ListActivitiesResponse404,
        ListActivitiesResponse500,
        list["ActivitiesCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ActivitiesCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListActivitiesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListActivitiesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListActivitiesResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListActivitiesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListActivitiesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListActivitiesResponse400,
        ListActivitiesResponse401,
        ListActivitiesResponse403,
        ListActivitiesResponse404,
        ListActivitiesResponse500,
        list["ActivitiesCollection"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListActivitiesResponse400,
        ListActivitiesResponse401,
        ListActivitiesResponse403,
        ListActivitiesResponse404,
        ListActivitiesResponse500,
        list["ActivitiesCollection"],
    ]
]:
    """List Activities

     Get the UBA (User Behavioral Analysis) activities.

    Args:
        event_type (Union[Unset, str]):
        ids (Union[Unset, str]):
        created_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListActivitiesResponse400, ListActivitiesResponse401, ListActivitiesResponse403, ListActivitiesResponse404, ListActivitiesResponse500, list['ActivitiesCollection']]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        ids=ids,
        created_after=created_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListActivitiesResponse400,
        ListActivitiesResponse401,
        ListActivitiesResponse403,
        ListActivitiesResponse404,
        ListActivitiesResponse500,
        list["ActivitiesCollection"],
    ]
]:
    """List Activities

     Get the UBA (User Behavioral Analysis) activities.

    Args:
        event_type (Union[Unset, str]):
        ids (Union[Unset, str]):
        created_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListActivitiesResponse400, ListActivitiesResponse401, ListActivitiesResponse403, ListActivitiesResponse404, ListActivitiesResponse500, list['ActivitiesCollection']]
    """

    return sync_detailed(
        client=client,
        event_type=event_type,
        ids=ids,
        created_after=created_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListActivitiesResponse400,
        ListActivitiesResponse401,
        ListActivitiesResponse403,
        ListActivitiesResponse404,
        ListActivitiesResponse500,
        list["ActivitiesCollection"],
    ]
]:
    """List Activities

     Get the UBA (User Behavioral Analysis) activities.

    Args:
        event_type (Union[Unset, str]):
        ids (Union[Unset, str]):
        created_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListActivitiesResponse400, ListActivitiesResponse401, ListActivitiesResponse403, ListActivitiesResponse404, ListActivitiesResponse500, list['ActivitiesCollection']]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        ids=ids,
        created_after=created_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListActivitiesResponse400,
        ListActivitiesResponse401,
        ListActivitiesResponse403,
        ListActivitiesResponse404,
        ListActivitiesResponse500,
        list["ActivitiesCollection"],
    ]
]:
    """List Activities

     Get the UBA (User Behavioral Analysis) activities.

    Args:
        event_type (Union[Unset, str]):
        ids (Union[Unset, str]):
        created_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListActivitiesResponse400, ListActivitiesResponse401, ListActivitiesResponse403, ListActivitiesResponse404, ListActivitiesResponse500, list['ActivitiesCollection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            event_type=event_type,
            ids=ids,
            created_after=created_after,
        )
    ).parsed
